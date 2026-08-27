import { useEffect, useState } from "react";
import {
  Plus,
  ArrowDownLeft,
  ArrowUpRight,
  X
} from "lucide-react";

import styles from "./Transactions.module.css";


const API = "http://localhost:8000";


const Transactions = () => {

  const [transactions, setTransactions] =
    useState([]);

  const [search, setSearch] =
    useState("");

  const [showForm, setShowForm] =
    useState(false);

  const [type, setType] =
    useState("Deposit");

  const [loading, setLoading] =
    useState(false);

  const [form, setForm] = useState({
    account: "",
    amount: "",
    description: ""
  });


  // Load transactions
  const loadTransactions = async () => {

    try {

      const response = await fetch(
        `${API}/transactions`
      );


      if (!response.ok) {

        throw new Error(
          "Failed to load transactions."
        );
      }


      const data =
        await response.json();


      setTransactions(
        Array.isArray(data)
          ? data
          : []
      );


    } catch (error) {

      console.error(
        "Transaction error:",
        error
      );

      alert(
        "Could not load transactions."
      );
    }
  };


  useEffect(() => {

    loadTransactions();

  }, []);


  // Search
  const filteredTransactions =
    transactions.filter(
      (transaction) => {

        const query =
          search
            .toLowerCase()
            .trim();


        return (

          transaction.transaction_id
            .toLowerCase()
            .includes(query)

          ||

          transaction.account_number
            .toLowerCase()
            .includes(query)

          ||

          transaction.transaction_type
            .toLowerCase()
            .includes(query)

          ||

          transaction.description
            .toLowerCase()
            .includes(query)

        );
      }
    );


  // Form change
  const handleChange = (e) => {

    const {
      name,
      value
    } = e.target;


    setForm({
      ...form,
      [name]: value
    });
  };


  // Create transaction
  const handleSubmit = async (e) => {

    e.preventDefault();


    if (
      !form.account.trim()
    ) {

      alert(
        "Please enter an account number."
      );

      return;
    }


    const numericAmount =
      Number(form.amount);


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
      type === "Deposit"
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
              form.account
                .trim()
                .toUpperCase(),

            amount:
              numericAmount,

            description:
              form.description.trim() ||
              type
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


      // Reset form
      setForm({
        account: "",
        amount: "",
        description: ""
      });


      setShowForm(false);


      // Get latest transactions
      await loadTransactions();


      alert(
        `${type} completed successfully.`
      );


    } catch (error) {

      alert(error.message);

    } finally {

      setLoading(false);
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
            Transactions
          </h1>

          <p>
            View deposits, withdrawals and transaction history.
          </p>

        </div>


        <button
          className={
            styles.addButton
          }
          onClick={() =>
            setShowForm(true)
          }
        >

          <Plus size={17} />

          New Transaction

        </button>

      </div>


      {/* Search */}

      <div
        className={
          styles.search
        }
      >

        <input
          type="text"
          placeholder="Search Transaction ID, Account or Type..."
          value={search}
          onChange={(e) =>
            setSearch(
              e.target.value
            )
          }
        />

      </div>


      {/* Table */}

      <div
        className={
          styles.tableCard
        }
      >

        <table>

          <thead>

            <tr>

              <th>
                ID
              </th>

              <th>
                Account
              </th>

              <th>
                Type
              </th>

              <th>
                Amount
              </th>

              <th>
                Balance After
              </th>

              <th>
                Description
              </th>

              <th>
                Date
              </th>

              <th>
                Status
              </th>

            </tr>

          </thead>


          <tbody>

            {filteredTransactions.map(
              (transaction) => {

                const isDeposit =
                  transaction.transaction_type ===
                  "DEPOSIT";


                return (

                  <tr
                    key={
                      transaction.transaction_id
                    }
                  >

                    <td
                      className={
                        styles.transactionId
                      }
                    >

                      {
                        transaction.transaction_id
                      }

                    </td>


                    <td>

                      {
                        transaction.account_number
                      }

                    </td>


                    <td>

                      <span
                        className={
                          styles.type
                        }
                      >

                        {isDeposit ? (

                          <ArrowDownLeft
                            size={14}
                          />

                        ) : (

                          <ArrowUpRight
                            size={14}
                          />

                        )}


                        {isDeposit
                          ? "Deposit"
                          : "Withdrawal"}

                      </span>

                    </td>


                    <td>

                      ETB{" "}

                      {Number(
                        transaction.amount
                      ).toLocaleString(
                        undefined,
                        {
                          minimumFractionDigits: 2,
                          maximumFractionDigits: 2
                        }
                      )}

                    </td>


                    <td>

                      ETB{" "}

                      {Number(
                        transaction.balance_after
                      ).toLocaleString(
                        undefined,
                        {
                          minimumFractionDigits: 2,
                          maximumFractionDigits: 2
                        }
                      )}

                    </td>


                    <td>

                      {
                        transaction.description
                      }

                    </td>


                    <td>

                      {transaction.timestamp
                        ? new Date(
                            transaction.timestamp
                          ).toLocaleString()
                        : "-"}

                    </td>


                    <td>

                      <span
                        className={
                          styles.status
                        }
                      >

                        {
                          transaction.status
                        }

                      </span>

                    </td>

                  </tr>

                );
              }
            )}


            {!filteredTransactions.length && (

              <tr>

                <td
                  colSpan="8"
                  className={
                    styles.empty
                  }
                >

                  {search
                    ? "No matching transactions found."
                    : "No transactions found."}

                </td>

              </tr>

            )}

          </tbody>

        </table>

      </div>


      {/* New Transaction Modal */}

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
                New Transaction
              </h2>


              <button
                onClick={() =>
                  setShowForm(false)
                }
              >

                <X size={20} />

              </button>

            </div>


            {/* Transaction Type */}

            <div
              className={
                styles.typeButtons
              }
            >

              <button
                type="button"
                className={
                  type === "Deposit"
                    ? styles.selected
                    : ""
                }
                onClick={() =>
                  setType(
                    "Deposit"
                  )
                }
              >
                Deposit
              </button>


              <button
                type="button"
                className={
                  type === "Withdrawal"
                    ? styles.selected
                    : ""
                }
                onClick={() =>
                  setType(
                    "Withdrawal"
                  )
                }
              >
                Withdraw
              </button>

            </div>


            <form
              onSubmit={
                handleSubmit
              }
            >

              <label>
                Account Number
              </label>


              <input
                type="text"
                name="account"
                placeholder="A001"
                required
                value={
                  form.account
                }
                onChange={
                  handleChange
                }
              />


              <label>
                Amount
              </label>


              <input
                type="number"
                name="amount"
                min="0.01"
                step="0.01"
                placeholder="Enter amount"
                required
                value={
                  form.amount
                }
                onChange={
                  handleChange
                }
              />


              <label>
                Description
              </label>


              <input
                type="text"
                name="description"
                placeholder="Optional"
                value={
                  form.description
                }
                onChange={
                  handleChange
                }
              />


              <button
                type="submit"
                className={
                  styles.saveButton
                }
                disabled={loading}
              >

                {loading
                  ? "Processing..."
                  : type}

              </button>


              <button
                type="button"
                className={
                  styles.cancelButton
                }
                onClick={() =>
                  setShowForm(false)
                }
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