export const landingPageRoutes = [
    {
        path: "",
        name: "landing",
        component: () => import("@/views/landing/index.vue"),
    },
]


export const allRoutes = [...landingPageRoutes]