<template>
  <div
    class="fixed pt-3 z-20 inset-0 focus:outline-none duration-500 bg-neutral-800"
    @click.self="close"
    tabindex="-1"
    @keydown.esc="close"
  >
    <div
      class="bg-neutral-200 z-50 rounded-lg w-[50vw] h-auto mx-auto xl:my-2 flex flex-col shadow-4xl relative"
    >
      <div class="z-50">
        <ModalWindowButtonClose @click="close" class="absolute right-0" />
      </div>
      <div class="flex justify-center pt-8">
        <p class="text-3xl font-bold">Добавить персонал</p>
      </div>
      <div class="w-full pt-12">
        <form
          class="flex flex-col gap-2 px-16 justify-center"
          @submit.prevent="submitPersonData"
        >
          <div class="flex items-center justify-between w-full gap-2">
            <p class="text-neutral-700 w-4/12 mb-1.5 font-semibold">
              Скан или фото документа:
            </p>
            <input
              multiple
              class="rounded-md w-8/12 h-8 pl-2.5 placeholder:text-sm file:rounded-xl file:w-[12vw] file:border-2 file:border-neutral-500 file:shadow-md file:mr-4"
              type="file"
              accept="image/png, image/jpeg"
              ref="fileInput"
              @change="updateFileInput"
              required
            />
          </div>
          <div
            v-if="filePreviews.length"
            class="flex flex-wrap mt-4 gap-2 justify-start"
          >
            <div
              v-for="(file, index) in filePreviews"
              :key="index"
              class="w-1/5"
            >
              <img
                :src="file"
                alt="preview"
                class="rounded-md shadow-md w-full cursor-pointer"
                @click="openImageInNewWindow(file)"
              />
            </div>
          </div>
          <div class="flex items-center justify-end w-full gap-2 mt-4">
            <button
              @click.prevent="submitPersonData"
              type="submit"
              class="bg-green-700 shadow-md mb-4 hover:bg-green-800 duration-300 hover:shadow-xl rounded-md px-4 py-2 text-neutral-200"
            >
              Отправить
            </button>
          </div>
          <transition
            enter-active-class="transition ease-in-out duration-500 transform"
            enter-from-class="translate-x-full"
            enter-to-class="translate-x-0"
            leave-active-class="transition ease-in-out duration-500 transform"
            leave-from-class="translate-x-0"
            leave-to-class="translate-x-full"
          >
            <Alert
              v-if="showAlert"
              :type="alertType"
              :title="alertTitle"
              :message="alertMessage"
              :visible="showAlert"
              @close="showAlert = false"
            />
          </transition>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import ModalWindowButtonClose from "./ModalWindowButtonClose.vue";
import Alert from "./Alert.vue";
import axios from "axios";

export default {
  components: {
    ModalWindowButtonClose,
    Alert,
  },
  methods: {
    close() {
      this.$emit("close");
    },
    updateFileInput(event) {
      this.files = Array.from(event.target.files);
      this.generateFilePreviews();
    },
    generateFilePreviews() {
      this.filePreviews = this.files.map((file) => URL.createObjectURL(file));
    },
    openImageInNewWindow(src) {
      window.open(src, "_blank");
    },
    async submitPersonData() {
      if (!this.validateForm()) {
        return;
      }
      const formData = new FormData();
      this.files.forEach((file) => {
        formData.append("files", file);
      });

      try {
        const response = await axios.post(
          "http://localhost:8000/uploadPeople",
          formData
        );
        this.alertType = "success";
        this.alertTitle = "Успешно";
        this.alertMessage = "Данные успешно отправлены!";
        this.showAlert = true;
        this.files = [];
        this.filePreviews = [];
        setTimeout(() => {
          this.showAlert = false;
          this.$emit("close");
        }, 4000);
        console.log(response.data);
      } catch (error) {
        this.alertType = "error";
        this.alertTitle = "Ошибка";
        this.alertMessage = "Ошибка при отправке данных";
        this.showAlert = true;
        console.error(error);
      }
    },
    validateForm() {
      if (!this.files.length) {
        this.alertType = "error";
        this.alertTitle = "Ошибка";
        this.alertMessage = "Все поля должны быть заполнены!";
        this.showAlert = true;
        return false;
      }
      return true;
    },
  },
  mounted() {
    this.$el.focus();
  },
  emits: ["close"],
  data() {
    return {
      files: [],
      filePreviews: [],
      successMessage: "",
      errorMessage: "",
      showAlert: false,
      alertType: "",
      alertTitle: "",
      alertMessage: "",
    };
  },
};
</script>

<style scoped>
.file-preview {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.file-preview img {
  width: 100%;
  height: auto;
  max-width: 100px;
  border-radius: 0.5rem;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  cursor: pointer;
}
</style>
