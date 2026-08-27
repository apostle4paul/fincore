import { useState } from "react";
import { Plus, MoreHorizontal } from "lucide-react";
import styles from "./Loans.module.css";

const Loans = () => {

  const [loans, setLoans] = useState([
    {
      id: "L001",
      member: "M001",
      amount: 50000,
      remaining: 35000,
      status: "Active"
    },
    {
      id: "L002",
      member: "M002",
      amount: 30000,
      remaining: 15000,
      status: "Active"
    },
    {
      id: "L003",
      member: "M003",
      amount: 20000,
      remaining: 0,
      status: "Paid"
    }
  ]);

  const [search, setSearch] = useState("");
  const [status, setStatus] = useState("All");
  const [showForm, setShowForm] = useState(false);
  const [selectedLoan, setSelectedLoan] = useState(null);

  const [form, setForm] = useState({
    member: "",
    amount: ""
  });


  const filteredLoans = loans.filter((loan) => {

    const matchesSearch =
      loan.id.toLowerCase().includes(search.toLowerCase()) ||
      loan.member.toLowerCase().includes(search.toLowerCase());

    const matchesStatus =
      status === "All" || loan.status === status;

    return matchesSearch && matchesStatus;
  });


  const handleSubmit = (e) => {

    e.preventDefault();

    const loan = {
      id: `L00${loans.length + 1}`,
      member: form.member.toUpperCase(),
      amount: Number(form.amount),
      remaining: Number(form.amount),
      status: "Active"
    };

    setLoans([...loans, loan]);

    setForm({
      member: "",
      amount: ""
    });

    setShowForm(false);
  };


  return (
    <div className={styles.page}>

      {/* Header */}

      <div className={styles.header}>

        <div>
          <p className={styles.label}>Banking</p>

          <h1>Loans</h1>

          <p>
            Manage member loans and outstanding balances.
          </p>
        </div>

        <button
          className={styles.addButton}
          onClick={() => setShowForm(true)}
        >
          <Plus size={17} />
          Add Loan
        </button>

      </div>


      {/* Search and Filter */}

      <div className={styles.toolbar}>

        <input
          type="text"
          placeholder="Search Loan ID or Member ID..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <select
          value={status}
          onChange={(e) => setStatus(e.target.value)}
        >
          <option value="All">All Status</option>
          <option value="Active">Active</option>
          <option value="Paid">Paid</option>
        </select>

      </div>


      {/* Table */}

      <div className={styles.tableCard}>

        <table>

          <thead>
            <tr>
              <th>Loan ID</th>
              <th>Member</th>
              <th>Amount</th>
              <th>Remaining</th>
              <th>Status</th>
              <th></th>
            </tr>
          </thead>

          <tbody>

            {filteredLoans.map((loan) => (

              <tr key={loan.id}>

                <td className={styles.loanId}>
                  {loan.id}
                </td>

                <td>
                  {loan.member}
                </td>

                <td>
                  ETB {loan.amount.toLocaleString()}
                </td>

                <td>
                  ETB {loan.remaining.toLocaleString()}
                </td>

                <td>

                  <span
                    className={
                      loan.status === "Active"
                        ? styles.active
                        : styles.paid
                    }
                  >
                    {loan.status}
                  </span>

                </td>

                <td className={styles.actions}>

                  <button
                    onClick={() => setSelectedLoan(loan)}
                  >
                    <MoreHorizontal size={18} />
                  </button>

                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>


      {/* Add Loan */}

      {showForm && (

        <div className={styles.overlay}>

          <div className={styles.form}>

            <h2>Add Loan</h2>

            <form onSubmit={handleSubmit}>

              <label>Member ID</label>

              <input
                required
                placeholder="M001"
                value={form.member}
                onChange={(e) =>
                  setForm({
                    ...form,
                    member: e.target.value
                  })
                }
              />

              <label>Loan Amount</label>

              <input
                required
                type="number"
                min="1"
                placeholder="Enter amount"
                value={form.amount}
                onChange={(e) =>
                  setForm({
                    ...form,
                    amount: e.target.value
                  })
                }
              />

              <button
                className={styles.saveButton}
                type="submit"
              >
                Create Loan
              </button>

              <button
                type="button"
                className={styles.cancelButton}
                onClick={() => setShowForm(false)}
              >
                Cancel
              </button>

            </form>

          </div>

        </div>

      )}


      {/* View Loan */}

      {selectedLoan && (

        <div className={styles.overlay}>

          <div className={styles.form}>

            <h2>Loan Details</h2>

            <p><strong>Loan ID:</strong> {selectedLoan.id}</p>

            <p><strong>Member:</strong> {selectedLoan.member}</p>

            <p>
              <strong>Amount:</strong> ETB{" "}
              {selectedLoan.amount.toLocaleString()}
            </p>

            <p>
              <strong>Remaining:</strong> ETB{" "}
              {selectedLoan.remaining.toLocaleString()}
            </p>

            <p>
              <strong>Status:</strong> {selectedLoan.status}
            </p>

            <button
              className={styles.cancelButton}
              onClick={() => setSelectedLoan(null)}
            >
              Close
            </button>

          </div>

        </div>

      )}

    </div>
  );
};

export default Loans;