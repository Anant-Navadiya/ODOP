const authRoutes = [
    {
        path: "/login",
        name: "Login",
        component: () => import("@/views/auth-pages/login.vue"),
    },
    {
        path: "/register",
        name: "Register",
        component: () => import("@/views/auth-pages/register.vue"),
    },
    {
        path: "/recoverpw",
        name: "Recover Password",
        component: () => import("@/views/auth-pages/recover-pass.vue"),
    },
    {
        path: "/lock-screen",
        name: "Lock Screen",
        component: () => import("@/views/auth-pages/lock-screen.vue"),
    },
];

const errorPageRoutes = [
    {
        path: "/404",
        name: "Error 404",
        component: () => import("@/views/pages/error-404.vue"),
    },
    {
        path: "/404-alt",
        name: "Error 404 Alt",
        component: () => import("@/views/pages/error-404-alt.vue"),
    },
    {
        path: "/500",
        name: "Error 500",
        component: () => import("@/views/pages/error-500.vue"),
    },
    // {
    //     path: "/:catchAll(.*)",
    //     redirect: "404",
    // },
]

const dashboardRoutes = [
    {
        path: "",
        name: "Dashboard",
        meta: {authRequired: true},
        component: () => import("@/views/dashboard/index.vue"),
    },
];

const productsRoutes = [
    {
        path: "/products",
        name: "Products",
        meta: {authRequired: true},
        children:[
            {
                path:'',
                name:'All Products',
                component: () => import("@/views/products/index.vue"),
            },
            {
                path:':category_slug/:product_slug/',
                name:'Product View',
                component: () => import("@/views/products/product-view.vue"),
            }
        ],

    },
];

const categoriesRoutes = [
    {
        path: "/categories",
        name: "Categories",
        meta: {authRequired: true},
        children:[
            // {
            //     path:'',
            //     name:'All Categories',
            //     component: () => import("@/views/products/index.vue"),
            // },
            {
                path:':category_slug',
                name:'Product View',
                component: () => import("@/views/categories/index.vue"),
            }
        ],

    },
];


export const authProtectedRoutes = [...dashboardRoutes,...categoriesRoutes,...productsRoutes]

export const allRoutes = [...authRoutes, ...errorPageRoutes, ...authProtectedRoutes];
