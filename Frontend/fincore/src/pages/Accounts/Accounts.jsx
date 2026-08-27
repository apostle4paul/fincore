import { useEffect, useState } from "react";
import {
  Plus,
  MoreHorizontal,
  X
} from "lucide-react";

import styles from "./Accounts.module.css";


const API = "http://localhost:8000";


const Accounts = () => {

  const [accounts, setAccounts] = useState([]);

  const [showForm, setShowForm] = useState(false);

  const [memberId, setMemberId] = useState("");

  const [menuId, setMenuId] = useState(null);

  const [transaction, setTransaction] = useState(null);

  const [amount, setAmount] = useState("");

  const [loading, setLoading] = useState(false);


  // Load accounts
  const loadAccounts = async () => {

    try {

      const response = await fetch(
        `${API}/accounts`
      );

      if (!response.ok) {

        throw new Error(
          "Failed to load accounts."
        );
      }

      const data = await response.json();

      setAccounts(
        Array.isArray(data)
          ? data
          : []
      );

    } catch (error) {

      console.error(
        "Accounts error:",
        error
      );

      alert(
        "Could not load accounts."
      );
    }
  };


  useEffect(() => {

    loadAccounts();

  }, []);


  // Open account
  const handleAdd = async (e) => {

    e.preventDefault();

    if (!memberId.trim()) {

      alert("Please enter a Member ID.");

      return;
    }

    setLoading(true);

    try {

      const response = await fetch(
        `${API}/accounts`,
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json"
          },

          body: JSON.stringify({
            member_id:
              memberId
                .trim()
                .toUpperCase()
          })
        }
      );

      const data = await response.json();

      if (!response.ok) {

        throw new Error(
          data.detail ||
          "Could not open account."
        );
      }

      setMemberId("");

      setShowForm(false);

      await loadAccounts();

      alert(
        `Account ${data.account_number} opened successfully.`
      );

    } catch (error) {

      alert(error.message);

    } finally {

      setLoading(false);
    }
  };


  // Deposit / Withdraw
  const handleTransaction = async (e) => {

    e.preventDefault();

    const numericAmount =
      Number(amount);

    if (
      !numericAmount ||
      numericAmount <= 0
    ) {

      alert(
        "Amount must be greater than zero."
      );

      return;
    }

    setLoading(true);

    const endpoint =
      transaction.type === "deposit"
        ? "/transactions/deposit"
        : "/transactions/withdraw";


    try {

      const response = await fetch(
        `${API}${endpoint}`,
        {
          method: "POST",

          headers: {
            "Content-Type":
              "application/json"
          },

          body: JSON.stringify({
            account_number:
              transaction.account_number,

            amount:
              numericAmount,

            description:
              transaction.type === "deposit"
                ? "Deposit"
                : "Withdrawal"
          })
        }
      );


      const data =
        await response.json();


      if (!response.ok) {

        throw new Error(
          data.detail ||
          "Transaction failed."
        );
      }


      setTransaction(null);

      setAmount("");

      setMenuId(null);


      // Reload account balances
      await loadAccounts();


      alert(
        `${
          transaction.type === "deposit"
            ? "Deposit"
            : "Withdrawal"
        } successful.`
      );


    } catch (error) {

      alert(error.message);

    } finally {

      setLoading(false);
    }
  };


  const openTransaction = (
    account,
    type
  ) => {

    setTransaction({
      account_number:
        account.account_number,

      type
    });

    setAmount("");

    setMenuId(null);
  };


  // Close account
  const handleCloseAccount = async (
    account
  ) => {

    if (
      !window.confirm(
        `Close account ${account.account_number}?`
      )
    ) {

      return;
    }


    try {

      const response = await fetch(
        `${API}/accounts/${account.account_number}/close`,
        {
          method: "POST"
        }
      );


      const data =
        await response.json();


      if (!response.ok) {

        throw new Error(
          data.detail ||
          "Could not close account."
        );
      }


      setMenuId(null);

      await loadAccounts();


      alert(
        `Account ${account.account_number} closed.`
      );


    } catch (error) {

      alert(error.message);
    }
  };


  return (

    <div className={styles.page}>

      {/* Header */}

      <div className={styles.header}>

        <div>

          <p className={styles.label}>
            Banking
          </p>

          <h1>
            Accounts
          </h1>

          <p>
            Manage member savings accounts.
          </p>

        </div>


        <button
          className={styles.addButton}
          onClick={() =>
            setShowForm(true)
          }
        >

          <Plus size={17} />

          Open Account

        </button>

      </div>


      {/* Table */}

      <div className={styles.tableCard}>

        <table>

          <thead>

            <tr>

              <th>
                Account Number
              </th>

              <th>
                Member ID
              </th>

              <th>
                Balance
              </th>

              <th>
                Status
              </th>

              <th>
                Actions
              </th>

            </tr>

          </thead>


          <tbody>

            {accounts.map(
              (account) => (

                <tr
                  key={
                    account.account_number
                  }
                >

                  <td
                    className={
                      styles.accountId
                    }
                  >
                    {
                      account.account_number
                    }
                  </td>


                  <td>
                    {
                      account.member_id
                    }
                  </td>


                  <td>

                    ETB{" "}

                    {Number(
                      account.balance || 0
                    ).toLocaleString(
                      undefined,
                      {
                        minimumFractionDigits: 2,
                        maximumFractionDigits: 2
                      }
                    )}

                  </td>


                  <td>

                    <span
                      className={
                        account.status ===
                        "ACTIVE"
                          ? styles.active
                          : styles.inactive
                      }
                    >

                      {
                        account.status
                      }

                    </span>

                  </td>


                  <td
                    className={
                      styles.actions
                    }
                  >

                    <button
                      onClick={() =>
                        setMenuId(
                          menuId ===
                          account.account_number
                            ? null
                            : account.account_number
                        )
                      }
                    >

                      <MoreHorizontal
                        size={18}
                      />

                    </button>


                    {menuId ===
                      account.account_number && (

                      <div
                        className={
                          styles.menu
                        }
                      >

                        <button
                          onClick={() =>
                            alert(
                              `Account: ${account.account_number}\n` +
                              `Member: ${account.member_id}\n` +
                              `Type: ${account.account_type}\n` +
                              `Balance: ETB ${Number(account.balance).toFixed(2)}\n` +
                              `Status: ${account.status}\n` +
                              `Opened: ${account.date_opened}`
                            )
                          }
                        >
                          View
                        </button>


                        {account.status ===
                          "ACTIVE" && (

                          <>
                            <button
                              onClick={() =>
                                openTransaction(
                                  account,
                                  "deposit"
                                )
                              }
                            >
                              Deposit
                            </button>


                            <button
                              onClick={() =>
                                openTransaction(
                                  account,
                                  "withdraw"
                                )
                              }
                            >
                              Withdraw
                            </button>


                            <button
                              onClick={() =>
                                handleCloseAccount(
                                  account
                                )
                              }
                            >
                              Close
                            </button>

                          </>
                        )}

                      </div>

                    )}

                  </td>

                </tr>

              )
            )}


            {!accounts.length && (

              <tr>

                <td
                  colSpan="5"
                  className={
                    styles.empty
                  }
                >
                  No accounts found.
                </td>

              </tr>

            )}

          </tbody>

        </table>

      </div>


      {/* Open Account Modal */}

      {showForm && (

        <div
          className={
            styles.overlay
          }
        >

          <div
            className={
              styles.form
            }
          >

            <div
              className={
                styles.formHeader
              }
            >

              <h2>
                Open Account
              </h2>


              <button
                onClick={() =>
                  setShowForm(false)
                }
              >

                <X size={20} />

              </button>

            </div>


            <form
              onSubmit={handleAdd}
            >

              <label>
                Member ID
              </label>


              <input
                value={memberId}
                onChange={(e) =>
                  setMemberId(
                    e.target.value
                  )
                }
                placeholder="M001"
                required
              />


              <button
                className={
                  styles.saveButton
                }
                type="submit"
                disabled={loading}
              >

                {loading
                  ? "Opening..."
                  : "Open Account"}

              </button>

            </form>

          </div>

        </div>

      )}


      {/* Deposit / Withdraw Modal */}

      {transaction && (

        <div
          className={
            styles.overlay
          }
        >

          <div
            className={
              styles.form
            }
          >

            <div
              className={
                styles.formHeader
              }
            >

              <h2>

                {transaction.type ===
                "deposit"
                  ? "Deposit"
                  : "Withdraw"}

              </h2>


              <button
                onClick={() =>
                  setTransaction(null)
                }
              >

                <X size={20} />

              </button>

            </div>


            <form
              onSubmit={
                handleTransaction
              }
            >

              <label>
                Account
              </label>


              <input
                value={
                  transaction.account_number
                }
                disabled
              />


              <label>
                Amount
              </label>


              <input
                type="number"
                min="0.01"
                step="0.01"
                value={amount}
                onChange={(e) =>
                  setAmount(
                    e.target.value
                  )
                }
                placeholder="Enter amount"
                required
              />


              <button
                className={
                  styles.saveButton
                }
                type="submit"
                disabled={loading}
              >

                {loading
                  ? "Processing..."
                  : "Confirm"}

              </button>

            </form>

          </div>

        </div>

      )}

    </div>
  );
};


export default Accounts;