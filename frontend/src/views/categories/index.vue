<template>
  <Layout>
    <div v-if="useEcom.isLoading" class="absolute left-[50%] top-[50%]">
      <div
          class="text-center animate-spin inline-block w-8 h-8 border-[3px] border-current border-t-transparent text-primary rounded-full mx-auto"
          role="status" aria-label="loading">
        <span class="sr-only">Loading...</span>
      </div>
    </div>

    <section v-if="!useEcom.isLoading" class="p-6">
      <div v-for="(category,idx) in categoriesData" :key="idx">
        <div class="text-2xl font-bold text-black ms-20 my-10">{{category.name}}s</div>
        <div class="grid lg:grid-cols-4 gap-6">
          <div class="mx-auto w-72" v-for="(product,idx) in category.products" :key="idx">
            <router-link :to="`/products${product.get_absolute_url}`">
              <div class="flex items-center justify-center ">
                <div class=" w-full">
                  <div class="bg-white shadow-xl rounded-lg overflow-hidden">
                    <div class="bg-cover bg-center h-56 p-4"
                         :style="{backgroundImage: `url(${product.get_thumbnail})`}">

                    </div>
                    <div class="p-4">
                      <p class="uppercase tracking-wide text-sm font-bold text-gray-700">{{ product.name }}</p>
                      <p class="text-3xl text-gray-900">₹{{ product.price }}</p>
                      <p class="text-gray-700">{{ product.description.slice(0, 50) }}...</p>
                    </div>

                    <div class="px-4 pt-3 pb-4 border-t border-gray-300 bg-gray-100">
                      <div class="text-xs uppercase font-bold text-gray-600 tracking-wide">Retailer</div>
                      <div class="flex items-center pt-2">
                        <img :src="product.get_thumbnail" class="bg-cover bg-center w-10 h-10 rounded-full mr-3"
                             alt=""/>

                        <div>
                          <p class="font-bold text-gray-900">Tiffany Heffner</p>
                          <p class="text-sm text-gray-700">(555) 555-4321</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </router-link>
          </div>

        </div>
      </div>
    </section>
  </Layout>
</template>

<script lang="ts">
import Layout from "@/components/layouts/layout.vue";
import axios from "axios";
import {useEcomStore} from "@/stores";

export default {
  components: {Layout},
  data() {
    return {
      categoriesData: [],
      useEcom: useEcomStore()
    };
  },

  mounted() {
    this.getCategories()
  },
  methods: {
    async getCategories() {
      this.useEcom.setIsLoading(true)
      const category_slug = this.$route.params.category_slug
      await axios.get(`/api/products/${category_slug}/`).then(res => this.categoriesData = res.data)
      this.useEcom.setIsLoading(false)
    }
  }
}
</script>
