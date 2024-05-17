<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500">
    <div class="fixed w-64 left-6">
      <SidebarMain />
    </div>
    <div
      class="flex flex-col duration-500 justify-center ml-72 items-center w-full bg-frameBackground rounded-xl outline-dashed outline-[1px] outline-outlineColor mb-4"
    >
      <div class="flex pt-10">
        <p
          class="text-center text-4xl font-black text-activeText duration-500 pb-1"
        >
          Трудовая книжка
        </p>
      </div>
      <div class="text-neutral-50 flex gap-4 pb-4">
        <p>Серия GP-4</p>
        <p>Номер 1234567</p>
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
                placeholder="Фамилия"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight dark:text-neutral-400 text-neutral-700 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Фамилия
              </label>
            </div>
            <!-- Имя -->
            <div class="relative h-11 w-full">
              <input
                placeholder="Имя"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight text-neutral-400 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Имя
              </label>
            </div>
            <!-- Отчество -->
            <div class="relative h-11 w-full">
              <input
                placeholder="Отчество"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight text-neutral-400 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Отчество
              </label>
            </div>
            <!-- Дата рождения -->
            <div class="relative h-11 w-full">
              <input
                placeholder="Дата рождения"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight text-neutral-400 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Дата рождения
              </label>
            </div>
            <!-- Образование -->
            <div class="relative h-11 w-full">
              <input
                placeholder="Образование"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight text-neutral-400 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Образование
              </label>
            </div>
            <!-- Профессия, специальность -->
            <div class="relative h-11 w-full">
              <input
                placeholder="Профессия, специальность"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight text-neutral-400 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Профессия, специальность
              </label>
            </div>
            <!-- Дата заполнения -->
            <div class="relative h-11 w-full">
              <input
                placeholder="Дата заполнения"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight text-neutral-400 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Дата заполнения
              </label>
            </div>
          </div>
          <!-- Если происходила смена ФИО -->
          <div class="min-w-[430px] flex flex-col gap-3">
            <p class="text-activeText font-semibold text-center">
              Происходила смена ФИО
            </p>
            <div class="relative h-11 w-full">
              <input
                placeholder="Фамилия"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight text-neutral-400 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Фамилия
              </label>
            </div>
            <!-- Имя -->
            <div class="relative h-11 w-full">
              <input
                placeholder="Имя"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight text-neutral-400 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Имя
              </label>
            </div>
            <!-- Отчество -->
            <div class="relative h-11 w-full">
              <input
                placeholder="Отчество"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight text-neutral-400 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Отчество
              </label>
            </div>
            <!-- Документ -->
            <div class="relative h-11 w-full">
              <input
                placeholder="Документ"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight text-neutral-400 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Документ
              </label>
            </div>
            <!-- Серия -->
            <div class="relative h-11 w-full">
              <input
                placeholder="Серия"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight text-neutral-400 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Серия
              </label>
            </div>
            <!-- Номер -->
            <div class="relative h-11 w-full">
              <input
                placeholder="Номер"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight text-neutral-400 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Номер
              </label>
            </div>
            <!-- Дата выдачи -->
            <div class="relative h-11 w-full">
              <input
                placeholder="Дата выдачи"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight text-neutral-400 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Дата выдачи
              </label>
            </div>
            <!-- Кем выдано -->
            <div class="relative h-11 w-full">
              <input
                placeholder="Кем выдано"
                class="peer h-full w-full border-b dark:border-neutral-200 border-neutral-900 bg-transparent pt-4 pb-2 font-sans text-lg font-normal text-activeText outline outline-0 transition-all placeholder-shown:border-neutral-400 placeholder:text-neutral-600 focus:border-neutral-200 focus:outline-0 disabled:border-0 disabled:bg-neutral-50 placeholder:opacity-0 focus:placeholder:opacity-100"
              />
              <label
                class="after:content[''] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none !overflow-visible truncate text-[14px] pt-1 font-normal leading-tight text-neutral-400 transition-all after:absolute after:-bottom-1.5 after:block after:w-full after:scale-x-0 after:border-b-2 after:border-neutral-200 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] dark:peer-placeholder-shown:text-neutral-200 peer-placeholder-shown:text-neutral-700 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-neutral-300 peer-focus:after:scale-x-100 peer-focus:after:border-neutral-300 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-neutral-100"
              >
                Кем выдано
              </label>
            </div>
          </div>
        </div>

        <!-- Таблица "РАЗДЕЛ СВЕДЕНИЯ О РАБОТЕ" -->
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
                v-for="i in 7"
                class="bg-transparent text-neutral-800 dark:text-neutral-300 border-t dark:border-t-neutral-200 border-t-neutral-700 dark:border-neutral-700 dark:hover:bg-neutral-600"
              >
                <td class="px-6 py-4">03.12.2024</td>
                <td class="px-6 py-4">04.12.2024</td>
                <td class="px-6 py-4 text-justify">
                  fugiat sed veniam dolorum dicta soluta. Perferendis distinctio
                  amet temporibus vero.
                </td>
                <td class="px-6 py-4 text-justify">
                  ratione odio provident earum quibusdam vero, perferendis
                  commodi vel libero a, quas placeat maiores optio inventore
                  possimus!
                </td>
                <td class="px-6 py-4 text-center">Приказ</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Таблица "РАЗДЕЛ СВЕДЕНИЯ О ПООЩРЕНИЯХ И НАГРАЖДЕНИЯХ" -->
        <p
          class="text-center text-4xl font-black text-activeText duration-500 py-4"
        >
          Сведения о поощрениях и награждениях
        </p>
        <div
          class="w-full mb-4 shadow-md border-[1px] border-neutral-700 dark:border-neutral-200 rounded-xl sm:rounded-lg"
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
                v-for="i in 7"
                class="bg-transparent text-neutral-800 dark:text-neutral-300 border-t dark:border-t-neutral-200 border-t-neutral-700 dark:border-neutral-700 dark:hover:bg-neutral-600"
              >
                <td class="px-6 py-4">03.12.2024</td>
                <td class="px-6 py-4 text-justify">
                  fugiat sed veniam dolorum dicta soluta. Perferendis distinctio
                  amet temporibus vero.
                </td>
                <td class="px-6 py-4 text-justify">
                  ratione odio provident earum quibusdam vero, perferendis
                  commodi vel libero a, quas placeat maiores optio inventore
                  possimus!
                </td>
                <td class="px-6 py-4 text-center">Приказ</td>
              </tr>
            </tbody>
          </table>
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
  emits: ["close"],
  methods: {
    async fetchPeople() {
      try {
        const response = await fetch("http://localhost:8000/getperson");
        if (!response.ok) {
          throw new Error("Failed to fetch data");
        }
        const data = await response.json();
        this.people = data.people;
        this.totalCount = data.total_count;
        console.log(this.people);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
    getImage(image_path) {
      return `http://localhost:8000/inputs/people/${image_path}`;
    },
  },
  mounted() {
    this.fetchPeople();
  },
};
</script>
