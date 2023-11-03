<template>
  <div class="card" v-for="(project, index) in projectAdditional" :key="index">
    <div class="p-6">
      <div class="flex items-center">
        <div class="flex-shrink-0 me-3">
          <div
              class="w-12 h-12 flex justify-center items-center rounded"
              :class="`text-${project.color} bg-${project.color}/25`"
          >
            <i :class="`${project.icon} text-xl`"></i>
          </div>
        </div>
        <div class="flex-grow">
          <h5 class="mb-1">{{ project.text }}</h5>
          <p>{{ project.subtext }}</p>
        </div>

        <div class="hs-dropdown relative inline-flex [--placement:left-top]">
          <button class="hs-dropdown-toggle text-gray-600 dark:text-gray-400" type="button">
            <i class="mgc_more_2_fill text-xl"></i>
          </button>

          <div class="hs-dropdown-menu transition-[opacity,margin] duration hs-dropdown-open:opacity-100 opacity-0 hidden w-36 z-50 mt-2 duration-300 bg-white dark:bg-gray-800 shadow-lg border border-gray-200 dark:border-gray-700 rounded-lg p-2">
            <a class="flex items-center gap-1.5 py-1.5 px-3.5 rounded text-sm transition-all duration-300 bg-transparent text-gray-800 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-gray-200" href="javascript:void(0)">
              Today
            </a>
            <a class="flex items-center gap-1.5 py-1.5 px-3.5 rounded text-sm transition-all duration-300 bg-transparent text-gray-800 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-gray-200" href="javascript:void(0)">
              Yesterday
            </a>
            <a class="flex items-center gap-1.5 py-1.5 px-3.5 rounded text-sm transition-all duration-300 bg-transparent text-gray-800 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-gray-300" href="javascript:void(0)">
              Last Week
            </a>
            <a class="flex items-center gap-1.5 py-1.5 px-3.5 rounded text-sm transition-all duration-300 bg-transparent text-gray-800 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-gray-300" href="javascript:void(0)">
              Last Month
            </a>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script lang="ts">

export default {
  data() {
    return {
      projectAdditional: [
        {
          icon: "mgc_document_2_line",
          color: "primary",
          text: "Active Projects",
          subtext: "85",
        },
        {
          icon: "mgc_group_line",
          color: "success",
          text: "Total Employees",
          subtext: "32",
        },
        {
          icon: "mgc_star_line",
          color: "info",
          text: "Project Reviews",
          subtext: "40",
        },
        {
          icon: "mgc_new_folder_line",
          color: "warning",
          text: "New Projects",
          subtext: "25",
        },
      ],
    }
  }
}
</script>
