import { useEffect, useState } from "react";
import { Plus, MoreHorizontal } from "lucide-react";
import styles from "./Loans.module.css";

const API = "http://127.0.0.1:8000/loans";

const Loans = () => {
  const [loans, setLoans] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [selectedLoan, setSelectedLoan] = useState(null);

  const [form, setForm] = useState({
    member_id: "",
    account_number: "",
    loan_type: "PERSONAL",
    amount: "",
    duration: ""
  });

  const [payment, setPayment] = useState("");

  // Get loans
  const loadLoans = async () => {
    try {
      const response = await fetch(API);
      const data = await response.json();
      setLoans(data);
    } catch (error) {
      console.error("Failed to load loans:", error);
    }
  };

  useEffect(() => {
    loadLoans();
  }, []);

  // Apply loan
  const applyLoan = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(API, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          member_id: form.member_id,
          account_number: form.account_number,
          loan_type: form.loan_type,
          amount: Number(form.amount),
          duration: Number(form.duration)
        })
      });

      const data = await response.json();

      if (!response.ok) {
        alert(data.detail);
        return;
      }

      alert("Loan application submitted.");

      setForm({
        member_id: "",
        account_number: "",
        loan_type: "PERSONAL",
        amount: "",
        duration: ""
      });

      setShowForm(false);
      loadLoans();

    } catch (error) {
      alert("Could not connect to the server.");
    }
  };

  // Approve loan
  const approveLoan = async (id) => {
    try {
      const response = await fetch(`${API}/${id}/approve`, {
        method: "POST"
      });

      const data = await response.json();

      if (!response.ok) {
        alert(data.detail);
        return;
      }

      alert("Loan approved.");
      loadLoans();
      setSelectedLoan(null);

    } catch (error) {
      alert("Could not connect to the server.");
    }
  };

  // Reject loan
  const rejectLoan = async (id) => {
    try {
      const response = await fetch(`${API}/${id}/reject`, {
        method: "POST"
      });

      const data = await response.json();

      if (!response.ok) {
        alert(data.detail);
        return;
      }

      alert("Loan rejected.");
      loadLoans();
      setSelectedLoan(null);

    } catch (error) {
      alert("Could not connect to the server.");
    }
  };

  // Make payment
  const makePayment = async () => {
    if (!payment || Number(payment) <= 0) {
      alert("Enter a valid payment amount.");
      return;
    }

    try {
      const response = await fetch(
        `${API}/${selectedLoan.loan_id}/payment`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            amount: Number(payment)
          })
        }
      );

      const data = await response.json();

      if (!response.ok) {
        alert(data.detail);
        return;
      }

      alert("Payment successful.");

      setPayment("");
      setSelectedLoan(null);
      loadLoans();

    } catch (error) {
      alert("Could not connect to the server.");
    }
  };

  return (
    <div className={styles.page}>

      {/* Header */}
      <div className={styles.header}>
        <div>
          <p className={styles.label}>Banking</p>
          <h1>Loans</h1>
          <p>Manage member loans and repayments.</p>
        </div>

        <button
          className={styles.addButton}
          onClick={() => setShowForm(true)}
        >
          <Plus size={17} />
          Add Loan
        </button>
      </div>

      {/* Loans Table */}
      <div className={styles.tableCard}>
        <table>
          <thead>
            <tr>
              <th>Loan ID</th>
              <th>Member</th>
              <th>Type</th>
              <th>Amount</th>
              <th>Paid</th>
              <th>Status</th>
              <th></th>
            </tr>
          </thead>

          <tbody>
            {loans.length === 0 ? (
              <tr>
                <td colSpan="7">
                  No loans found.
                </td>
              </tr>
            ) : (
              loans.map((loan) => (
                <tr key={loan.loan_id}>
                  <td className={styles.loanId}>
                    {loan.loan_id}
                  </td>

                  <td>{loan.borrower}</td>

                  <td>{loan.loan_type}</td>

                  <td>
                    ETB {loan.amount.toLocaleString()}
                  </td>

                  <td>
                    ETB {loan.amount_paid.toLocaleString()}
                  </td>

                  <td>
                    <span
                      className={
                        loan.status === "APPROVED"
                          ? styles.active
                          : loan.status === "PAID"
                          ? styles.paid
                          : styles.pending
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
              ))
            )}
          </tbody>
        </table>
      </div>

      {/* Apply Loan Form */}
      {showForm && (
        <div className={styles.overlay}>
          <div className={styles.form}>
            <h2>Apply for Loan</h2>

            <form onSubmit={applyLoan}>

              <label>Member ID</label>
              <input
                required
                placeholder="M001"
                value={form.member_id}
                onChange={(e) =>
                  setForm({
                    ...form,
                    member_id: e.target.value
                  })
                }
              />

              <label>Account Number</label>
              <input
                required
                placeholder="A001"
                value={form.account_number}
                onChange={(e) =>
                  setForm({
                    ...form,
                    account_number: e.target.value
                  })
                }
              />

              <label>Loan Type</label>
              <select
                value={form.loan_type}
                onChange={(e) =>
                  setForm({
                    ...form,
                    loan_type: e.target.value
                  })
                }
              >
                <option value="PERSONAL">
                  Personal
                </option>

                <option value="BUSINESS">
                  Business
                </option>
              </select>

              <label>Loan Amount</label>
              <input
                required
                type="number"
                min="1"
                value={form.amount}
                onChange={(e) =>
                  setForm({
                    ...form,
                    amount: e.target.value
                  })
                }
              />

              <label>Duration (months)</label>
              <input
                required
                type="number"
                min="1"
                value={form.duration}
                onChange={(e) =>
                  setForm({
                    ...form,
                    duration: e.target.value
                  })
                }
              />

              <button
                className={styles.saveButton}
                type="submit"
              >
                Apply Loan
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

      {/* Loan Details */}
      {selectedLoan && (
        <div className={styles.overlay}>
          <div className={styles.form}>

            <h2>Loan Details</h2>

            <p>
              <strong>Loan ID:</strong>{" "}
              {selectedLoan.loan_id}
            </p>

            <p>
              <strong>Member:</strong>{" "}
              {selectedLoan.borrower}
            </p>

            <p>
              <strong>Account:</strong>{" "}
              {selectedLoan.account_number}
            </p>

            <p>
              <strong>Type:</strong>{" "}
              {selectedLoan.loan_type}
            </p>

            <p>
              <strong>Amount:</strong> ETB{" "}
              {selectedLoan.amount.toLocaleString()}
            </p>

            <p>
              <strong>Interest:</strong>{" "}
              {selectedLoan.interest_rate * 100}%
            </p>

            <p>
              <strong>Duration:</strong>{" "}
              {selectedLoan.duration} months
            </p>

            <p>
              <strong>Total Repayment:</strong> ETB{" "}
              {(
                selectedLoan.amount +
                selectedLoan.amount *
                  selectedLoan.interest_rate
              ).toLocaleString()}
            </p>

            <p>
              <strong>Remaining:</strong> ETB{" "}
              {(
                selectedLoan.amount +
                selectedLoan.amount *
                  selectedLoan.interest_rate -
                selectedLoan.amount_paid
              ).toLocaleString()}
            </p>

            <p>
              <strong>Status:</strong>{" "}
              {selectedLoan.status}
            </p>

            {/* Approve / Reject */}
            {selectedLoan.status === "PENDING" && (
              <>
                <button
                  className={styles.saveButton}
                  onClick={() =>
                    approveLoan(selectedLoan.loan_id)
                  }
                >
                  Approve Loan
                </button>

                <button
                  className={styles.cancelButton}
                  onClick={() =>
                    rejectLoan(selectedLoan.loan_id)
                  }
                >
                  Reject Loan
                </button>
              </>
            )}

            {/* Payment */}
            {selectedLoan.status === "APPROVED" && (
              <>
                <label>Payment Amount</label>

                <input
                  type="number"
                  min="1"
                  placeholder="Enter payment"
                  value={payment}
                  onChange={(e) =>
                    setPayment(e.target.value)
                  }
                />

                <button
                  className={styles.saveButton}
                  onClick={makePayment}
                >
                  Make Payment
                </button>
              </>
            )}

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