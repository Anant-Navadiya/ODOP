<script lang="ts">
export default {
  props: {
    title: String,
  },
  mounted() {
    this.useMeta({
      title: this.title,
    });
  }
};
</script>
