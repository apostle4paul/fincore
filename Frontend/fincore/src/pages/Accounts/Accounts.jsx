import { useEffect, useState } from "react";
import { Plus, MoreHorizontal, X } from "lucide-react";
import styles from "./Accounts.module.css";

const API = "http://localhost:8000";

const Accounts = () => {
  const [accounts, setAccounts] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [memberId, setMemberId] = useState("");
  const [menuId, setMenuId] = useState(null);

  const [transaction, setTransaction] = useState(null);
  const [amount, setAmount] = useState("");

  const loadAccounts = async () => {
    try {
      const response = await fetch(`${API}/accounts`);
      const data = await response.json();

      setAccounts(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    loadAccounts();
  }, []);

  // Open account
  const handleAdd = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(`${API}/accounts`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          member_id: memberId.trim().toUpperCase(),
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Could not open account");
      }

      setMemberId("");
      setShowForm(false);

      await loadAccounts();
    } catch (error) {
      alert(error.message);
    }
  };

  // Deposit / Withdraw
  const handleTransaction = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(
        `${API}/accounts/${transaction.account_number}/${transaction.type}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            amount: Number(amount),
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Transaction failed");
      }

      setTransaction(null);
      setAmount("");
      setMenuId(null);

      await loadAccounts();
    } catch (error) {
      alert(error.message);
    }
  };

  const openTransaction = (account, type) => {
    setTransaction({
      account_number: account.account_number,
      type,
    });

    setAmount("");
    setMenuId(null);
  };

  return (
    <div className={styles.page}>

      <div className={styles.header}>
        <div>
          <p className={styles.label}>Banking</p>
          <h1>Accounts</h1>
          <p>Manage member savings accounts.</p>
        </div>

        <button
          className={styles.addButton}
          onClick={() => setShowForm(true)}
        >
          <Plus size={17} />
          Open Account
        </button>
      </div>

      <div className={styles.tableCard}>
        <table>
          <thead>
            <tr>
              <th>Account Number</th>
              <th>Member ID</th>
              <th>Balance</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>
            {accounts.map((account) => (
              <tr key={account.account_number}>

                <td className={styles.accountId}>
                  {account.account_number}
                </td>

                <td>{account.member_id}</td>

                <td>
                  ETB {Number(account.balance || 0).toLocaleString()}
                </td>

                <td>
                  <span
                    className={
                      account.status === "ACTIVE"
                        ? styles.active
                        : styles.inactive
                    }
                  >
                    {account.status}
                  </span>
                </td>

                <td className={styles.actions}>
                  <button
                    onClick={() =>
                      setMenuId(
                        menuId === account.account_number
                          ? null
                          : account.account_number
                      )
                    }
                  >
                    <MoreHorizontal size={18} />
                  </button>

                  {menuId === account.account_number && (
                    <div className={styles.menu}>

                      <button
                        onClick={() =>
                          alert(
                            `Account: ${account.account_number}\n` +
                            `Member: ${account.member_id}\n` +
                            `Balance: ETB ${account.balance}\n` +
                            `Status: ${account.status}`
                          )
                        }
                      >
                        View
                      </button>

                      <button
                        onClick={() =>
                          openTransaction(account, "deposit")
                        }
                      >
                        Deposit
                      </button>

                      <button
                        onClick={() =>
                          openTransaction(account, "withdraw")
                        }
                      >
                        Withdraw
                      </button>

                    </div>
                  )}
                </td>

              </tr>
            ))}

            {!accounts.length && (
              <tr>
                <td colSpan="5" className={styles.empty}>
                  No accounts found.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      {/* Open Account */}

      {showForm && (
        <div className={styles.overlay}>
          <div className={styles.form}>

            <div className={styles.formHeader}>
              <h2>Open Account</h2>

              <button onClick={() => setShowForm(false)}>
                <X size={20} />
              </button>
            </div>

            <form onSubmit={handleAdd}>
              <label>Member ID</label>

              <input
                value={memberId}
                onChange={(e) => setMemberId(e.target.value)}
                placeholder="M001"
                required
              />

              <button
                className={styles.saveButton}
                type="submit"
              >
                Open Account
              </button>
            </form>

          </div>
        </div>
      )}

      {/* Deposit / Withdraw */}

      {transaction && (
        <div className={styles.overlay}>
          <div className={styles.form}>

            <div className={styles.formHeader}>
              <h2>
                {transaction.type === "deposit"
                  ? "Deposit"
                  : "Withdraw"}
              </h2>

              <button onClick={() => setTransaction(null)}>
                <X size={20} />
              </button>
            </div>

            <form onSubmit={handleTransaction}>

              <label>Amount</label>

              <input
                type="number"
                min="0.01"
                step="0.01"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                placeholder="Enter amount"
                required
              />

              <button
                className={styles.saveButton}
                type="submit"
              >
                Confirm
              </button>

            </form>

          </div>
        </div>
      )}

    </div>
  );
};

export default Accounts;