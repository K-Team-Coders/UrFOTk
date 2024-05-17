<template>
  <div v-if="visible" class="fixed right-0 bottom-1 py-2 z-50">
    <div :class="alertClasses" role="alert">
      <div class="relative">
        <BaseIcon
          name="x"
          class="w-6 h-6 absolute -right-2 -top-2 cursor-pointer"
          @click="close"
        />
      </div>
      <p class="font-bold text-xl">{{ title }}</p>
      <p class="text-lg">{{ message }}</p>
    </div>
  </div>
</template>

<script>
import BaseIcon from "./BaseIcon.vue";

export default {
  components: { BaseIcon },
  props: {
    type: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    message: {
      type: String,
      required: true,
    },
    visible: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    alertClasses() {
      return {
        "bg-red-200 border-l-4 border-red-500 text-red-700 p-4 w-96":
          this.type === "error",
        "bg-green-200 border-l-4 border-green-500 text-green-700 p-4 w-96":
          this.type === "success",
      };
    },
  },
  methods: {
    close() {
      this.$emit("close");
    },
  },
};
</script>
