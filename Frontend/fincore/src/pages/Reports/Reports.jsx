import { useState } from "react";
import styles from "./Reports.module.css";

const Reports = () => {

  const [generated, setGenerated] = useState(false);

  const summary = {
    members: 120,
    accounts: 156,
    transactions: 438,
    loans: 32,
    loanAmount: 1250000
  };

  const generateReport = () => {
    setGenerated(true);
  };

  return (
    <div className={styles.page}>

      {/* Header */}

      <div className={styles.header}>

        <div>
          <p className={styles.label}>Analytics</p>

          <h1>Reports</h1>

          <p>
            View basic banking activity and financial summaries.
          </p>
        </div>

        <button
          className={styles.button}
          onClick={generateReport}
        >
          Generate Report
        </button>

      </div>


      {/* Summary */}

      <div className={styles.cards}>

        <div className={styles.card}>
          <span>Members</span>
          <strong>{summary.members}</strong>
        </div>

        <div className={styles.card}>
          <span>Accounts</span>
          <strong>{summary.accounts}</strong>
        </div>

        <div className={styles.card}>
          <span>Transactions</span>
          <strong>{summary.transactions}</strong>
        </div>

        <div className={styles.card}>
          <span>Loans</span>
          <strong>{summary.loans}</strong>
        </div>

      </div>


      {/* Loan Summary */}

      <div className={styles.section}>

        <h2>Loan Summary</h2>

        <div className={styles.row}>
          <span>Total Loans</span>
          <strong>{summary.loans}</strong>
        </div>

        <div className={styles.row}>
          <span>Total Loan Amount</span>
          <strong>
            ETB {summary.loanAmount.toLocaleString()}
          </strong>
        </div>

      </div>


      {/* Report */}

      {generated && (

        <div className={styles.section}>

          <h2>Transaction Report</h2>

          <table>

            <thead>
              <tr>
                <th>Category</th>
                <th>Total</th>
              </tr>
            </thead>

            <tbody>

              <tr>
                <td>Deposits</td>
                <td>ETB 850,000</td>
              </tr>

              <tr>
                <td>Withdrawals</td>
                <td>ETB 420,000</td>
              </tr>

              <tr>
                <td>Loan Disbursements</td>
                <td>ETB 1,250,000</td>
              </tr>

            </tbody>

          </table>

        </div>

      )}

    </div>
  );
};

export default Reports;