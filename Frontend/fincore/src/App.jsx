import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import DashboardLayout from "./layouts/DashboardLayout";

import Dashboard from "./pages/Dashboard/Dashboard";
import Members from "./pages/Members/Members";
import Accounts from "./pages/Accounts/Accounts";
import Transactions from "./pages/Transactions/Transactions";
import Loans from "./pages/Loans/Loans";
import Reports from "./pages/Reports/Reports";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<DashboardLayout />}
        >

          <Route
            index
            element={<Dashboard />}
          />

          <Route
            path="members"
            element={<Members />}
          />

          <Route
            path="accounts"
            element={<Accounts />}
          />

          <Route
            path="transactions"
            element={<Transactions />}
          />

          <Route
            path="loans"
            element={<Loans />}
          />

          <Route
            path="reports"
            element={<Reports />}
          />

        </Route>

      </Routes>

    </BrowserRouter>
  );
}

export default App;