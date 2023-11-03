<template>
  <header class="app-header flex items-center px-4 gap-3">

    <router-link to="/" class="">

      <div class="logo-dark">
        <img
            src="@/assets/images/logo-dark.png"
            class="logo-lg h-6"
            alt="Dark logo"
        />

      </div>
    </router-link>

    <button
        type="button"
        data-hs-overlay="#topbar-search-modal"
        class="nav-link p-2 me-auto"
    >
      <span class="sr-only">Search</span>
      <span class="flex items-center justify-center h-6 w-6">
        <i class="mgc_search_line text-2xl"></i>
      </span>
    </button>


    <div class="flex">
      <router-link to="/" class="flex items-center py-2 px-5 rounded-md text-md text-black font-medium active">Home
      </router-link>
      <router-link to="/products" class="flex items-center py-2 px-5 rounded-md text-md text-black font-medium">Products
      </router-link>
      <router-link to="/" class="flex items-center py-2 px-5 rounded-md text-md text-black font-medium ">Community
      </router-link>
      <router-link to="/" class="flex items-center py-2 px-5 rounded-md text-md text-black font-medium ">Blogs
      </router-link>
    </div>

    <div class="flex space-x-2">
      <button type="button" class="btn bg-primary text-white">
        LogIn
      </button>
      <button
          type="button"
          class="btn border-success text-success hover:bg-success hover:text-white"
      >
        SignIn
      </button>
    </div>
  </header>

  <!-- Topbar Search Modal -->
  <div>
    <div
        id="topbar-search-modal"
        class="hs-overlay hidden w-full h-full fixed top-0 start-0 z-[60]"
    >
      <div
          class="hs-overlay-open:opacity-100 hs-overlay-open:duration-500 opacity-0 transition-all sm:max-w-lg sm:w-full m-12 sm:mx-auto"
      >
        <div
            class="mx-auto max-w-2xl overflow-hidden rounded-xl bg-white shadow-2xl transition-all dark:bg-slate-800"
        >
          <div class="relative">
            <div
                class="pointer-events-none absolute top-3.5 start-4 text-gray-900 text-opacity-40 dark:text-gray-200"
            >
              <i class="mgc_search_line text-xl"></i>
            </div>
            <input
                type="search"
                class="h-12 w-full border-0 bg-transparent ps-11 pe-4 text-gray-900 placeholder-gray-500 dark:placeholder-gray-300 dark:text-gray-200 focus:ring-0 sm:text-sm"
                placeholder="Search..."
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {SimpleBar} from "simplebar-vue3";


export default {
  components: {SimpleBar}
};
</script>

<style scoped>
.active {
  color: #546ee5;
}
</style>