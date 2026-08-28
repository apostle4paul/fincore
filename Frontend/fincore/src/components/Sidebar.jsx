import {
  LayoutDashboard,
  Users,
  WalletCards,
  ArrowLeftRight,
  Landmark
} from "lucide-react";

import { NavLink } from "react-router-dom";
import styles from "./Sidebar.module.css";

const Sidebar = () => {

  const navigation = [
    {
      title: "Overview",
      items: [
        {
          name: "Dashboard",
          path: "/",
          icon: LayoutDashboard
        }
      ]
    },

    {
      title: "Banking",
      items: [
        {
          name: "Members",
          path: "/members",
          icon: Users
        },
        {
          name: "Accounts",
          path: "/accounts",
          icon: WalletCards
        },
        {
          name: "Transactions",
          path: "/transactions",
          icon: ArrowLeftRight
        }
      ]
    },

    {
      title: "Credit",
      items: [
        {
          name: "Loans",
          path: "/loans",
          icon: Landmark
        }
      ]
    }
  ];

  return (
    <aside className={styles.sidebar}>

      {/* Logo */}
      <div className={styles.logo}>

        <div className={styles.logoMark}>
          F
        </div>

        <div className={styles.logoText}>
          <h2>FinCore</h2>
          <span>Banking System</span>
        </div>

      </div>

      {/* Navigation */}
      <nav className={styles.navigation}>

        {navigation.map((section) => (

          <div
            className={styles.section}
            key={section.title}
          >

            <p className={styles.sectionTitle}>
              {section.title}
            </p>

            {section.items.map((item) => {

              const Icon = item.icon;

              return (
                <NavLink
                  key={item.path}
                  to={item.path}
                  className={({ isActive }) =>
                    `${styles.navItem} ${
                      isActive ? styles.active : ""
                    }`
                  }
                >

                  <Icon size={19} />

                  <span>
                    {item.name}
                  </span>

                </NavLink>
              );

            })}

          </div>

        ))}

      </nav>

    </aside>
  );
};

export default Sidebar;