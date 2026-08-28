import { useEffect, useState } from "react";
import axios from "axios";
import { Plus, Search, Eye, Pencil, X } from "lucide-react";
import styles from "./Members.module.css";

const API_URL = "http://localhost:8000/members/members";

const Members = () => {
  const [members, setMembers] = useState([]);
  const [search, setSearch] = useState("");
  const [showForm, setShowForm] = useState(false);
  const [selectedMember, setSelectedMember] = useState(null);
  const [editing, setEditing] = useState(false);

  const [form, setForm] = useState({
    full_name: "",
    phone: "",
    email: ""
  });

  // Load members
  const getMembers = async () => {
    try {
      const response = await axios.get(API_URL);
      setMembers(response.data);
    } catch (error) {
      console.error("Error loading members:", error);
    }
  };

  useEffect(() => {
    getMembers();
  }, []);

  // Search
  const filteredMembers = members.filter((member) => {
    const text = search.toLowerCase();

    return (
      member.member_id.toLowerCase().includes(text) ||
      member.full_name.toLowerCase().includes(text) ||
      member.phone.includes(text) ||
      member.email.toLowerCase().includes(text)
    );
  });

  // Form input
  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  // Add member
  const addMember = () => {
    setEditing(false);
    setForm({
      full_name: "",
      phone: "",
      email: ""
    });
    setShowForm(true);
  };

  // Edit member
  const editMember = (member) => {
    setEditing(true);
    setSelectedMember(member);

    setForm({
      full_name: member.full_name,
      phone: member.phone,
      email: member.email
    });

    setShowForm(true);
  };

  // Save member
  const saveMember = async (e) => {
    e.preventDefault();

    try {
      if (editing) {
        await axios.put(
          `${API_URL}/${selectedMember.member_id}`,
          form
        );
      } else {
        await axios.post(API_URL, form);
      }

      setShowForm(false);
      setSelectedMember(null);
      getMembers();

    } catch (error) {
      console.error(error);
      alert(
        error.response?.data?.detail ||
        "Something went wrong."
      );
    }
  };

  // Deactivate member
  const deactivateMember = async (id) => {
    if (!window.confirm("Deactivate this member?")) {
      return;
    }

    try {
      await axios.put(`${API_URL}/${id}/deactivate`);
      getMembers();
    } catch (error) {
      console.error(error);
      alert(
        error.response?.data?.detail ||
        "Could not deactivate member."
      );
    }
  };

  return (
    <div className={styles.page}>

      {/* Header */}
      <div className={styles.header}>
        <div>
          <p className={styles.label}>BANKING</p>
          <h1>Members</h1>
          <p>Manage registered bank members.</p>
        </div>

        <button
          className={styles.addButton}
          onClick={addMember}
        >
          <Plus size={18} />
          Add Member
        </button>
      </div>

      {/* Search */}
      <div className={styles.toolbar}>
        <div className={styles.search}>
          <Search size={18} />

          <input
            placeholder="Search members..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </div>
      </div>

      {/* Table */}
      <div className={styles.tableCard}>
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Phone</th>
              <th>Email</th>
              <th>Date Joined</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>
            {filteredMembers.map((member) => (
              <tr key={member.member_id}>

                <td>{member.member_id}</td>
                <td>{member.full_name}</td>
                <td>{member.phone}</td>
                <td>{member.email}</td>
                <td>{member.date_joined}</td>

                <td>
                  <span
                    className={
                      member.status === "ACTIVE"
                        ? styles.active
                        : styles.inactive
                    }
                  >
                    {member.status}
                  </span>
                </td>

                <td className={styles.actions}>

                  <button
                    onClick={() =>
                      setSelectedMember(member)
                    }
                    title="View"
                  >
                    <Eye size={17} />
                  </button>

                  <button
                    onClick={() => editMember(member)}
                    title="Edit"
                  >
                    <Pencil size={17} />
                  </button>

                  {member.status === "ACTIVE" && (
                    <button
                      onClick={() =>
                        deactivateMember(member.member_id)
                      }
                      title="Deactivate"
                    >
                      <X size={17} />
                    </button>
                  )}

                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {filteredMembers.length === 0 && (
          <p className={styles.empty}>
            No members found.
          </p>
        )}
      </div>

      {/* Add / Edit Form */}
      {showForm && (
        <div className={styles.overlay}>
          <div className={styles.modal}>

            <div className={styles.modalHeader}>
              <h2>
                {editing ? "Edit Member" : "Add Member"}
              </h2>

              <button
                onClick={() => setShowForm(false)}
              >
                <X />
              </button>
            </div>

            <form onSubmit={saveMember}>

              <label>Full Name</label>
              <input
                name="full_name"
                value={form.full_name}
                onChange={handleChange}
                required
              />

              <label>Phone</label>
              <input
                name="phone"
                value={form.phone}
                onChange={handleChange}
                required
              />

              <label>Email</label>
              <input
                type="email"
                name="email"
                value={form.email}
                onChange={handleChange}
                required
              />

              <button
                className={styles.saveButton}
                type="submit"
              >
                {editing ? "Update Member" : "Save Member"}
              </button>

            </form>
          </div>
        </div>
      )}

      {/* Member Details */}
      {selectedMember && !showForm && (
        <div className={styles.overlay}>
          <div className={styles.modal}>

            <div className={styles.modalHeader}>
              <h2>Member Details</h2>

              <button
                onClick={() => setSelectedMember(null)}
              >
                <X />
              </button>
            </div>

            <div className={styles.details}>
              <p>
                <strong>ID:</strong>{" "}
                {selectedMember.member_id}
              </p>

              <p>
                <strong>Name:</strong>{" "}
                {selectedMember.full_name}
              </p>

              <p>
                <strong>Phone:</strong>{" "}
                {selectedMember.phone}
              </p>

              <p>
                <strong>Email:</strong>{" "}
                {selectedMember.email}
              </p>

              <p>
                <strong>Date Joined:</strong>{" "}
                {selectedMember.date_joined}
              </p>

              <p>
                <strong>Status:</strong>{" "}
                {selectedMember.status}
              </p>
            </div>

            <button
              className={styles.saveButton}
              onClick={() => setSelectedMember(null)}
            >
              Close
            </button>

          </div>
        </div>
      )}

    </div>
  );
};

export default Members;