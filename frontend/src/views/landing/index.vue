<template>

    <header class="app-header flex items-center px-4 gap-3 justify-between">

      <!-- Topbar Brand Logo -->
      <a href="index.html" class="logo-box">
        <!-- Light Brand Logo -->
        <div class="logo-light">
          <img src="@/assets/images/logo-light.png" class="logo-lg h-6" alt="Light logo">
        </div>

        <!-- Dark Brand Logo -->
        <div class="logo-dark">
          <img src="@/assets/images/logo-dark.png" class="logo-lg h-6" alt="Dark logo">
        </div>
      </a>

      <!-- Light/Dark Toggle Button -->
      <div class="flex ">
        <button id="light-dark-mode" type="button" class="nav-link p-2">
          <span class="sr-only">Light/Dark Mode</span>
          <span class="flex items-center justify-center h-6 w-6">
          <i class="mgc_moon_line text-2xl"></i>
        </span>
        </button>
      </div>

    </header>


    <section class="max-w-screen-2xl mx-auto p-10 h-[calc(100vh-70px)]">
      <div class="space-y-4">
        <h1 class="text-7xl text-slate-900 dark:text-slate-200 text-center">One District One Product</h1>
        <h4 class="text-base text-slate-900 dark:text-slate-200">One District One Product (ODOP) initiative is aimed at fostering balanced regional development across all
          districts of the country. The initiative aims to select, brand, and promote at least One Product from each
          District (One District - One Product) of the country for enabling holistic socioeconomic growth across all
          regions. The ODOP Initiative has identified a total of 1102 products from 761 districts across the
          country.</h4>
        <h4 class="text-base text-slate-900 dark:text-slate-200">Under the ODOP initiative, all products have been selected by States/UTs by taking into consideration the existing ecosystem on the ground, products identified under Districts as Export Hubs (DEH), and GI-tagged products. The finalized list is communicated to DPIIT by the relevant Department of States/UTs. All activities including exhibitions, capacity building, etc. are undertaken at the State/UT and district level, in consultation and coordination with the States/UTs.</h4>
      </div>
    </section>

    <section class="card">
      <div class="p-6 ">

      </div>
    </section>

</template>

<script lang="ts">
import {useLayoutStore} from "@/stores/layout";

export default {
  mounted() {
    useLayoutStore().initConfig();
  }
}
</script>
