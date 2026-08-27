import { useState } from "react";
import { Plus, ArrowDownLeft, ArrowUpRight } from "lucide-react";
import styles from "./Transactions.module.css";

const Transactions = () => {

  const [transactions, setTransactions] = useState([
    {
      id: "T001",
      account: "A001",
      type: "Deposit",
      amount: 5000,
      description: "Cash deposit",
      status: "Completed"
    },
    {
      id: "T002",
      account: "A002",
      type: "Withdrawal",
      amount: 2000,
      description: "ATM withdrawal",
      status: "Completed"
    },
    {
      id: "T003",
      account: "A001",
      type: "Deposit",
      amount: 3500,
      description: "Salary",
      status: "Completed"
    }
  ]);

  const [search, setSearch] = useState("");
  const [showForm, setShowForm] = useState(false);
  const [type, setType] = useState("Deposit");

  const [form, setForm] = useState({
    account: "",
    amount: "",
    description: ""
  });


  const filteredTransactions = transactions.filter((transaction) =>
    transaction.id.toLowerCase().includes(search.toLowerCase()) ||
    transaction.account.toLowerCase().includes(search.toLowerCase())
  );


  const handleSubmit = (e) => {
    e.preventDefault();

    const transaction = {
      id: `T00${transactions.length + 1}`,
      account: form.account.toUpperCase(),
      type,
      amount: Number(form.amount),
      description: form.description || type,
      status: "Completed"
    };

    setTransactions([...transactions, transaction]);

    setForm({
      account: "",
      amount: "",
      description: ""
    });

    setShowForm(false);
  };


  return (
    <div className={styles.page}>

      {/* Header */}

      <div className={styles.header}>

        <div>
          <p className={styles.label}>Banking</p>

          <h1>Transactions</h1>

          <p>
            View deposits, withdrawals and transaction history.
          </p>
        </div>

        <button
          className={styles.addButton}
          onClick={() => setShowForm(true)}
        >
          <Plus size={17} />
          New Transaction
        </button>

      </div>


      {/* Search */}

      <div className={styles.search}>
        <input
          type="text"
          placeholder="Search Transaction ID or Account ID..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>


      {/* Table */}

      <div className={styles.tableCard}>

        <table>

          <thead>
            <tr>
              <th>ID</th>
              <th>Account</th>
              <th>Type</th>
              <th>Amount</th>
              <th>Description</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>

            {filteredTransactions.map((transaction) => (

              <tr key={transaction.id}>

                <td className={styles.transactionId}>
                  {transaction.id}
                </td>

                <td>
                  {transaction.account}
                </td>

                <td>

                  <span className={styles.type}>

                    {transaction.type === "Deposit" ? (
                      <ArrowDownLeft size={14} />
                    ) : (
                      <ArrowUpRight size={14} />
                    )}

                    {transaction.type}

                  </span>

                </td>

                <td>
                  ETB {transaction.amount.toLocaleString()}
                </td>

                <td>
                  {transaction.description}
                </td>

                <td>
                  <span className={styles.status}>
                    {transaction.status}
                  </span>
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>


      {/* Transaction Form */}

      {showForm && (

        <div className={styles.overlay}>

          <div className={styles.form}>

            <h2>New Transaction</h2>

            <div className={styles.typeButtons}>

              <button
                type="button"
                className={type === "Deposit" ? styles.selected : ""}
                onClick={() => setType("Deposit")}
              >
                Deposit
              </button>

              <button
                type="button"
                className={type === "Withdrawal" ? styles.selected : ""}
                onClick={() => setType("Withdrawal")}
              >
                Withdraw
              </button>

            </div>


            <form onSubmit={handleSubmit}>

              <label>Account ID</label>

              <input
                type="text"
                placeholder="A001"
                required
                value={form.account}
                onChange={(e) =>
                  setForm({
                    ...form,
                    account: e.target.value
                  })
                }
              />


              <label>Amount</label>

              <input
                type="number"
                min="1"
                placeholder="Enter amount"
                required
                value={form.amount}
                onChange={(e) =>
                  setForm({
                    ...form,
                    amount: e.target.value
                  })
                }
              />


              <label>Description</label>

              <input
                type="text"
                placeholder="Optional"
                value={form.description}
                onChange={(e) =>
                  setForm({
                    ...form,
                    description: e.target.value
                  })
                }
              />


              <button
                type="submit"
                className={styles.saveButton}
              >
                {type}
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

    </div>
  );
};

export default Transactions;