<template>
  <Layout>
    <Breadcrumb title="Starter Page" subtitle="Extra Pages" />
  </Layout>
</template>

<script lang="ts">
import Layout from "@/components/layouts/layout.vue";
import Breadcrumb from "@/components/page-title.vue";
export default {
  components: { Layout, Breadcrumb },
};
</script>
