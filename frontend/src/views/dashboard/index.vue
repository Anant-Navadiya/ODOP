<template>
  <Layout>
    <div class="">
      <Swiper
          :slides-per-view="1"
          :modules="[Autoplay]"
          :autoplay="{delay:3000}"
          :loop="true"
          :pagination="true"
          class="h-screen"
      >
        <SwiperSlide>
          <div class="relative bg-cover h-[80vh] "
               :style="{backgroundImage: `url(${banner1})`}"
          >
            <div class="absolute inset-0 bg-black/50"></div>
            <div class="flex h-full items-center justify-center">
              <div class="text-center max-w-2xl mx-auto relative">
                <div class="flex justify-center">
                  <div class="w-16 h-16 rounded-full bg-white/10 flex items-center justify-center">
                    <i class="mdi mdi-rocket-launch text-3xl text-white"></i>
                  </div>
                </div>
                <h1 class="md:text-5xl/snug text-3xl font-semibold text-white mt-10">Integrate
                  Salesforce with The Apps You Use.</h1>
                <p class="text-base font-normal text-white/50 mt-5">At vero eos et accusamus et iusto
                  odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atqued
                  corrupti quos dolores et quas molestias excepturi sintoccaecati cupiditate.</p>

                <div class="mt-10">
                  <a href="#"
                     class="inline-flex items-center justify-center gap-2 py-3 px-7 rounded-md text-lg font-normal text-white bg-primary focus:text-gray-800 transition-all">Get
                    Started</a>
                </div>
              </div>
            </div>
          </div>
        </SwiperSlide>
        <SwiperSlide>
          <div class="relative bg-cover h-[80vh] "
               :style="{backgroundImage: `url(${banner2})`}"
          >
            <div class="absolute inset-0 bg-black/50"></div>
            <div class="flex h-full items-center justify-center">
              <div class="text-center max-w-2xl mx-auto relative">
                <div class="flex justify-center">
                  <div class="w-16 h-16 rounded-full bg-white/10 flex items-center justify-center">
                    <i class="mdi mdi-rocket-launch text-3xl text-white"></i>
                  </div>
                </div>
                <h1 class="md:text-5xl/snug text-3xl font-semibold text-white mt-10">Integrate
                  Salesforce with The Apps You Use.</h1>
                <p class="text-base font-normal text-white/50 mt-5">At vero eos et accusamus et iusto
                  odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atqued
                  corrupti quos dolores et quas molestias excepturi sintoccaecati cupiditate.</p>

                <div class="mt-10">
                  <a href="#"
                     class="inline-flex items-center justify-center gap-2 py-3 px-7 rounded-md text-lg font-normal text-white bg-primary focus:text-gray-800 transition-all">Get
                    Started</a>
                </div>
              </div>
            </div>
          </div>
        </SwiperSlide>
        <SwiperSlide>
          <div class="relative bg-cover h-[80vh] "
               :style="{backgroundImage: `url(${banner3})`}"
          >
            <div class="absolute inset-0 bg-black/50"></div>
            <div class="flex h-full items-center justify-center">
              <div class="text-center max-w-2xl mx-auto relative">
                <div class="flex justify-center">
                  <div class="w-16 h-16 rounded-full bg-white/10 flex items-center justify-center">
                    <i class="mdi mdi-rocket-launch text-3xl text-white"></i>
                  </div>
                </div>
                <h1 class="md:text-5xl/snug text-3xl font-semibold text-white mt-10">Integrate
                  Salesforce with The Apps You Use.</h1>
                <p class="text-base font-normal text-white/50 mt-5">At vero eos et accusamus et iusto
                  odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atqued
                  corrupti quos dolores et quas molestias excepturi sintoccaecati cupiditate.</p>

                <div class="mt-10">
                  <a href="#"
                     class="inline-flex items-center justify-center gap-2 py-3 px-7 rounded-md text-lg font-normal text-white bg-primary focus:text-gray-800 transition-all">Get
                    Started</a>
                </div>
              </div>
            </div>
          </div>
        </SwiperSlide>
      </Swiper>
    </div>

  </Layout>
</template>

<script lang="ts">
import Layout from "@/components/layouts/layout.vue";
import {Swiper, SwiperSlide} from 'swiper/vue';
import {Autoplay} from 'swiper/modules';

import banner1 from '@/assets/images/banner/bg-1.jpg'
import banner2 from '@/assets/images/banner/bg-2.jpg'
import banner3 from '@/assets/images/banner/bg-3.png'

export default {
  components: {
    Swiper,
    SwiperSlide,
    Layout,
  },
  data() {
    return {
      Autoplay,
      banner1,
      banner2,
      banner3,
    };
  },
};
</script>
