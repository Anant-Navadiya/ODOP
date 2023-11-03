<template>
  <div class="flex wrapper">
    <div class="page-content">
      <Topbar />
      <main class="flex-grow">
        <slot></slot>
      </main>
      <Footer />
    </div>
  </div>
</template>

<script lang="ts">
import Topbar from "./partials/topbar.vue";
import Footer from "./partials/footer.vue";
export default {
  components: { Topbar, Footer },
};
</script>
