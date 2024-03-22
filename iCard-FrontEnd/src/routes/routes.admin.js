import {HomeAdmin, Routers, Switches, Sites, SearchMac } from '../pages/Admin';
import {AdminLayout} from "../layouts";
import {UserAdmin} from "../pages/Admin/UserAdmin";

const routesAdmin = [
    {
        path: "/admin",
        layout: AdminLayout,
        component: HomeAdmin,
    },
    {
        path: "/admin/users",
        layout: AdminLayout,
        component: UserAdmin,
    },
    {
        path: "/admin/routers",
        layout: AdminLayout,
        component: Routers,
    },
    {
        path: "/admin/switches",
        layout: AdminLayout,
        component: Switches,
    },
    {
        path: "/admin/sites",
        layout: AdminLayout,
        component: Sites,
    },
    {
        path: "/admin/search",
        layout: AdminLayout,
        component: SearchMac,
    },
];

export default routesAdmin;