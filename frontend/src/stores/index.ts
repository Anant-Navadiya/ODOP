import {defineStore} from "pinia";
import axios from "axios";
import {useStorage} from "@vueuse/core";

export const useEcomStore = defineStore("ecom", {

    state: () => ({
        // authUser: useStorage('authUser', null),
        cart: useStorage('cart', {
            items: [],
        }),
        isAuthenticated: false,
        token: '',
        isLoading: false
    }),

    getters: {},

    actions: {
        addToCart(item:any) {

            const exists = this.cart.items.filter(i => i.product.id === item.product.id)

            if (exists.length) {
                exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
            } else {
                this.cart.items.push(item)
            }
        },
        setIsLoading(status: boolean) {
            this.isLoading = status
        }
    }
})