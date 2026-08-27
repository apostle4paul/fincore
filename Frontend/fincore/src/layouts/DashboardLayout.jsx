import { Outlet } from "react-router-dom";

import Sidebar from "../components/Sidebar";

import styles from "./DashboardLayout.module.css";

const DashboardLayout = () => {
  return (
    <div className={styles.layout}>

      <Sidebar />

      <div className={styles.main}>


        <main className={styles.content}>
          <Outlet />
        </main>

      </div>

    </div>
  );
};

export default DashboardLayout;