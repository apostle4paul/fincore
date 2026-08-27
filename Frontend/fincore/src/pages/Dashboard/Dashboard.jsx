import styles from "./Dashboard.module.css";

const Dashboard = () => {
  return (
    <div className={styles.dashboard}>
      <div className={styles.content}>
        <p>FINCORE BANKING</p>

        <h1>
          Simple Banking.
          <br />
          Smarter Finance.
        </h1>

        <span>
          Manage members, accounts, transactions, and loans
        </span>
      </div>
    </div>
  );
};

export default Dashboard;