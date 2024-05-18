<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500">
    <div class="fixed w-64 left-6">
      <SidebarMain />
    </div>
    <div
      class="flex flex-col duration-500 justify-center ml-72 items-center w-full bg-frameBackground rounded-xl outline-dashed outline-[1px] outline-outlineColor mb-4"
    >
      <div class="flex pt-10">
        <p class="text-center text-4xl font-black text-activeText duration-500">
          Трудовая книжка
        </p>
      </div>
      <div class="text-activeText flex gap-4 pb-8 pt-3">
        <div class="relative h-11 w-full">
          <input
            v-model="personData.series"
            placeholder="Например: AT-4"
            :class="inputFieldClass"
          />
          <label :class="labelFieldClass"> Серия </label>
        </div>
        <div class="relative h-11 w-full">
          <input
            v-model="personData.number"
            placeholder="Фамилия"
            :class="inputFieldClass"
          />
          <label :class="labelFieldClass"> Номер </label>
        </div>
      </div>

      <!-- Форма для сохранения данных -->
      <form class="w-10/12">
        <!-- Данные о персоне -->
        <div class="flex justify-between">
          <!-- Всегда -->
          <div class="min-w-[430px] flex flex-col gap-3">
            <p class="text-activeText font-semibold text-center">
              <br />
            </p>
            <!-- Фамилия -->
            <div class="relative h-11 w-full">
              <input
                v-model="personData.lastName"
                placeholder="Фамилия"
                :class="inputFieldClass"
              />
              <label :class="labelFieldClass"> Фамилия </label>
            </div>
            <!-- Имя -->
            <div class="relative h-11 w-full">
              <input
                v-model="personData.firstName"
                placeholder="Имя"
                :class="inputFieldClass"
              />
              <label :class="labelFieldClass"> Имя </label>
            </div>
            <!-- Отчество -->
            <div class="relative h-11 w-full">
              <input
                v-model="personData.patronymic"
                placeholder="Отчество"
                :class="inputFieldClass"
              />
              <label :class="labelFieldClass"> Отчество </label>
            </div>
            <!-- Дата рождения -->
            <div class="relative h-11 w-full">
              <input
                v-model="personData.birthday"
                placeholder="Дата рождения"
                :class="inputFieldClass"
              />
              <label :class="labelFieldClass"> Дата рождения </label>
            </div>

            <!-- Дата заполнения -->
            <div class="relative h-11 w-full">
              <input
                v-model="personData.fillDate"
                placeholder="Дата заполнения"
                :class="inputFieldClass"
              />
              <label :class="labelFieldClass"> Дата заполнения </label>
            </div>
          </div>
          <!-- Если происходила смена ФИО -->
          <div class="min-w-[430px] flex flex-col gap-3">
            <p class="text-activeText font-semibold text-center">
              Происходила смена ФИО
            </p>
            <div class="relative h-11 w-full">
              <input
                v-model="personData.changeSurname"
                placeholder="Фамилия"
                :class="inputFieldClass"
              />
              <label :class="labelFieldClass"> Фамилия </label>
            </div>
            <!-- Имя -->
            <div class="relative h-11 w-full">
              <input
                v-model="personData.changeName"
                placeholder="Имя"
                :class="inputFieldClass"
              />
              <label :class="labelFieldClass"> Имя </label>
            </div>
            <!-- Отчество -->
            <div class="relative h-11 w-full">
              <input
                v-model="personData.changePatronymic"
                placeholder="Отчество"
                :class="inputFieldClass"
              />
              <label :class="labelFieldClass"> Отчество </label>
            </div>
            <!-- Документ -->
            <div class="relative h-11 w-full">
              <input
                v-model="personData.changeDoc"
                placeholder="Документ"
                :class="inputFieldClass"
              />
              <label :class="labelFieldClass"> Документ </label>
            </div>
            <!-- Серия -->
            <div class="relative h-11 w-full">
              <input
                v-model="personData.docSerial"
                placeholder="Серия"
                :class="inputFieldClass"
              />
              <label :class="labelFieldClass"> Серия </label>
            </div>
            <!-- Номер -->
            <div class="relative h-11 w-full">
              <input
                v-model="personData.docNumber"
                placeholder="Номер"
                :class="inputFieldClass"
              />
              <label :class="labelFieldClass"> Номер </label>
            </div>
            <!-- Дата выдачи -->
            <div class="relative h-11 w-full">
              <input
                v-model="personData.deliveryDate"
                placeholder="Дата выдачи"
                :class="inputFieldClass"
              />
              <label :class="labelFieldClass"> Дата выдачи </label>
            </div>
            <!-- Кем выдано -->
            <div class="relative h-11 w-full">
              <input
                v-model="personData.whoDelivery"
                placeholder="Кем выдано"
                :class="inputFieldClass"
              />
              <label :class="labelFieldClass"> Кем выдано </label>
            </div>
          </div>
        </div>

        <!-- Сведения о работе -->
        <p
          class="text-center text-4xl font-black text-activeText duration-500 py-4"
        >
          Сведения о работе
        </p>
        <div
          class="w-full shadow-md border-[1px] border-neutral-700 dark:border-neutral-200 rounded-xl sm:rounded-lg"
        >
          <table class="w-full text-sm text-neutral-500 dark:text-neutral-200">
            <thead
              class="text-xs text-neutral-800 text-center bg-transparent border-b-[1px] dark:text-neutral-300"
            >
              <tr class="">
                <th scope="col" class="px-6 py-3">Дата приема</th>
                <th scope="col" class="px-6 py-3">Дата увольнения</th>
                <th scope="col" class="px-6 py-3">
                  Расшифровка печати (штампа)
                </th>
                <th scope="col" class="px-6 py-3">Расшифровка должности</th>
                <th scope="col" class="px-6 py-3">Приказ (номер и дата)</th>
              </tr>
            </thead>
            <tbody class="text-center">
              <tr
                v-for="(record, index) in workRecords"
                :key="index"
                class="bg-transparent text-neutral-800 dark:text-neutral-300 border-t dark:border-t-neutral-200 border-t-neutral-700 dark:border-neutral-700 dark:hover:bg-neutral-600"
              >
                <td
                  class="px-6 py-4"
                  contenteditable
                  @input="
                    updateWorkRecord(
                      index,
                      'startDate',
                      $event.target.innerText
                    )
                  "
                >
                  {{ record.startDate }}
                </td>
                <td
                  class="px-6 py-4"
                  contenteditable
                  @input="
                    updateWorkRecord(index, 'endDate', $event.target.innerText)
                  "
                >
                  {{ record.endDate }}
                </td>
                <td
                  class="px-6 py-4 text-justify"
                  contenteditable
                  @input="
                    updateWorkRecord(
                      index,
                      'sealExplanation',
                      $event.target.innerText
                    )
                  "
                >
                  {{ record.sealExplanation }}
                </td>
                <td
                  class="px-6 py-4 text-justify"
                  contenteditable
                  @input="
                    updateWorkRecord(
                      index,
                      'positionExplanation',
                      $event.target.innerText
                    )
                  "
                >
                  {{ record.positionExplanation }}
                </td>
                <td
                  class="px-6 py-4 text-center"
                  contenteditable
                  @input="
                    updateWorkRecord(
                      index,
                      'orderInfo',
                      $event.target.innerText
                    )
                  "
                >
                  {{ record.orderInfo }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="flex justify-end">
          <button
            @click="addWorkRecord"
            class="pr-1 text-sm text-activeText rounded"
          >
            Создать новую строку
          </button>
        </div>
        <!-- Сведения о поощрениях и награждениях -->
        <p
          class="text-center text-4xl font-black text-activeText duration-500 py-4"
        >
          Сведения о поощрениях и награждениях
        </p>
        <div
          class="w-full shadow-md border-[1px] border-neutral-700 dark:border-neutral-200 rounded-xl sm:rounded-lg"
        >
          <table class="w-full text-sm text-neutral-500 dark:text-neutral-200">
            <thead
              class="text-xs text-neutral-800 text-center bg-transparent border-b-[1px] dark:text-neutral-300"
            >
              <tr class="">
                <th scope="col" class="px-6 py-3">Дата приема</th>
                <th scope="col" class="px-6 py-3">
                  Расшифровка печати (штампа)
                </th>
                <th scope="col" class="px-6 py-3">
                  Расшифровка информации о поощрении и вознаграждении
                </th>
                <th scope="col" class="px-6 py-3">Приказ (номер и дата)</th>
              </tr>
            </thead>
            <tbody class="text-center">
              <tr
                v-for="(reward, index) in rewardRecords"
                :key="index"
                class="bg-transparent text-neutral-800 dark:text-neutral-300 border-t dark:border-t-neutral-200 border-t-neutral-700 dark:border-neutral-700 dark:hover:bg-neutral-600"
              >
                <td
                  class="px-6 py-4"
                  contenteditable
                  @input="
                    updateRewardRecord(
                      index,
                      'rewardDate',
                      $event.target.innerText
                    )
                  "
                >
                  {{ reward.rewardDate }}
                </td>
                <td
                  class="px-6 py-4 text-justify"
                  contenteditable
                  @input="
                    updateRewardRecord(
                      index,
                      'sealExplanation',
                      $event.target.innerText
                    )
                  "
                >
                  {{ reward.sealExplanation }}
                </td>
                <td
                  class="px-6 py-4 text-justify"
                  contenteditable
                  @input="
                    updateRewardRecord(
                      index,
                      'rewardExplanation',
                      $event.target.innerText
                    )
                  "
                >
                  {{ reward.rewardExplanation }}
                </td>
                <td
                  class="px-6 py-4 text-center"
                  contenteditable
                  @input="
                    updateRewardRecord(
                      index,
                      'orderInfo',
                      $event.target.innerText
                    )
                  "
                >
                  {{ reward.orderInfo }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="flex justify-end mb-4">
          <button
            @click="addRewardRecord"
            class="pr-1 text-sm text-activeText rounded"
          >
            Создать новую строку
          </button>
        </div>
        <div class="flex justify-end mb-4">
          <button
            class="align-middle select-none font-sans font-bold text-center uppercase transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 px-6 rounded-lg bg-red-800 text-neutral-50 shadow-md shadow-red-600/10 hover:shadow-lg hover:shadow-red-600/20 active:opacity-[0.75] flex items-center gap-3"
            type="button"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="2"
              stroke="currentColor"
              class="w-5 h-5"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 16.5V9.75m0 0l3 3m-3-3l-3 3M6.75 19.5a4.5 4.5 0 01-1.41-8.775 5.25 5.25 0 0110.233-2.33 3 3 0 013.758 3.848A3.752 3.752 0 0118 19.5H6.75z"
              ></path>
            </svg>
            Изменить и сохранить
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import TextOutput from "./TextOutput.vue";
import SmallLoader from "./SmallLoader.vue";
import BaseIcon from "./BaseIcon.vue";
import SidebarMain from "./SidebarMain.vue";
import ModalWindow from "./ModalWindow.vue";
import axios from "axios";
export default {
  components: {
    TextOutput,
    SmallLoader,
    BaseIcon,
    ModalWindow,
    SidebarMain,
  },
  props: {
    userData: {
      type: Object,
      default: () => ({}),
    },
  },
  data() {
    return {
      personData: {
        id: "",
        series: "",
        number: "",
        lastName: "",
        firstName: "",
        patronymic: "",
        birthday: "",
        fillDate: "",
        changeSurname: "",
        changeName: "",
        changePatronymic: "",
        changeDoc: "",
        docSerial: "",
        docNumber: "",
        deliveryDate: "",
        whoDelivery: "",
      },

      workRecords: [
        {
          startDate: "",
          endDate: "",
          sealExplanation: "",
          positionExplanation: "",
          orderInfo: "",
        },
      ],
      rewardRecords: [
        {
          rewardDate: "",
          sealExplanation: "",
          rewardExplanation: "",
          orderInfo: "",
        },
      ],
    };
  },
  methods: {
    updateWorkRecord(index, field, value) {
      this.workRecords[index][field] = value;
    },
    updateRewardRecord(index, field, value) {
      this.rewardRecords[index][field] = value;
    },
    addWorkRecord() {
      this.workRecords.push({
        startDate: "",
        endDate: "",
        sealExplanation: "",
        positionExplanation: "",
        orderInfo: "",
      });
    },
    addRewardRecord() {
      this.rewardRecords.push({
        rewardDate: "",
        sealExplanation: "",
        rewardExplanation: "",
        orderInfo: "",
      });
    },
    saveData() {
      // Здесь вы можете сохранить измененные данные
      console.log(this.workRecords);
      console.log(this.rewardRecords);

      // Пример отправки данных на сервер
      axios
        .post("http://your-server-url/api/save", {
          personData: this.personData,
          workRecords: this.workRecords,
          rewardRecords: this.rewardRecords,
        })
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  mounted() {
    // Проверка, если данные переданы через роут
    if (this.$route.state && this.$route.state.userData) {
      console.log("Received data:", this.$route.state.userData);
      this.personData.series = "";
      this.personData.number = "";
      this.personData.lastName = "";
      this.personData.firstName = "";
      this.personData.patronymic = "";
      this.personData.birthday = "";
      this.personData.fillDate = "";
      this.personData.changeSurname = "";
      this.personData.changeName = "";
      this.personData.changePatronymic = "";
      this.personData.changeDoc = "";
      this.personData.docSerial = "";
      this.personData.docNumber = "";
      this.personData.deliveryDate = "";
      this.personData.whoDelivery = "";
      this.workRecords.startDate = "";
      this.workRecords.endDate = "";
      this.workRecords.sealExplanation = "";
      this.workRecords.positionExplanation = "";
      this.workRecords.orderInfo = "";
      this.rewardRecords.rewardDate = "";
      this.rewardRecords.sealExplanation = "";
      this.rewardRecords.rewardExplanation = "";
      this.rewardRecords.orderInfo = "";
    }
  },
  watch: {
    $route(to, from) {
      if (to.state && to.state.userData) {
        console.log("Route changed, received data:", to.state.userData);
        this.personData = to.state.userData.personData || this.personData;
        this.workRecords = to.state.userData.workRecords || this.workRecords;
        this.rewardRecords =
          to.state.userData.rewardRecords || this.rewardRecords;
      }
    },
  },
  computed: {
    inputFieldClass() {
      return [
        "peer",
        "h-full",
        "w-full",
        "border-b",
        "placeholder:text-base",
        "dark:border-neutral-200",
        "border-neutral-900",
        "bg-transparent",
        "pt-4",
        "pb-2",
        "font-sans",
        "text-lg",
        "font-normal",
        "text-activeText",
        "outline",
        "outline-0",
        "transition-all",
        "placeholder-shown:border-neutral-400",
        "placeholder:text-neutral-600",
        "focus:border-neutral-200",
        "focus:outline-0",
        "disabled:border-0",
        "disabled:bg-neutral-50",
        "placeholder:opacity-0",
        "focus:placeholder:opacity-100",
      ];
    },
    labelFieldClass() {
      return [
        "pointer-events-none",
        "absolute",
        "left-0",
        "-top-1.5",
        "flex",
        "h-full",
        "w-full",
        "select-none",
        "!overflow-visible",
        "truncate",
        "text-[14px]",
        "pt-1",
        "font-normal",
        "leading-tight",
        "dark:text-neutral-400",
        "text-neutral-700",
        "transition-all",
        "after:absolute",
        "after:-bottom-1.5",
        "after:block",
        "after:w-full",
        "after:scale-x-0",
        "after:border-b-2",
        "after:border-neutral-200",
        "after:transition-transform",
        "after:duration-300",
        "peer-placeholder-shown:text-sm",
        "peer-placeholder-shown:leading-[4.25]",
        "dark:peer-placeholder-shown:text-neutral-200",
        "peer-placeholder-shown:text-neutral-700",
        "peer-focus:text-[11px]",
        "peer-focus:leading-tight",
        "peer-focus:text-neutral-300",
        "peer-focus:after:scale-x-100",
        "peer-focus:after:border-neutral-300",
        "peer-disabled:text-transparent",
        "peer-disabled:peer-placeholder-shown:text-neutral-100",
      ];
    },
  },
};
</script>
