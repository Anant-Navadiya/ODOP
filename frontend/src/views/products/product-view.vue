<template>
  <Layout>
    <div v-if="useEcom.isLoading" class="absolute left-[50%] top-[40%]">
      <div
          class="text-center animate-spin inline-block w-8 h-8 border-[3px] border-current border-t-transparent text-primary rounded-full mx-auto"
           role="status" aria-label="loading">
        <span class="sr-only">Loading...</span>
      </div>
    </div>

    <div v-if="isAdded"
         class="max-w-xs bg-white border rounded-md shadow-lg dark:bg-gray-800 dark:border-gray-700 absolute right-10 top-24"
         role="alert">
      <div class="flex p-4">
        <div class="flex-shrink-0">
          <svg class="h-4 w-4 text-green-500 mt-0.5" xmlns="http://www.w3.org/2000/svg" width="16" height="16"
               fill="currentColor" viewBox="0 0 16 16">
            <path
                d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
          </svg>
        </div>
        <div class="ml-3">
          <p class="text-sm text-gray-700 dark:text-gray-400">
            The product was added to cart.
          </p>
        </div>
      </div>
    </div>

    <section v-if="!useEcom.isLoading" class="py-6">
      <div class="container mt-5 lg:mt-10">
        <div class="grid xl:grid-cols-12 gap-12">
          <div class="lg:col-span-6">
            <div class="grid grid-cols-12 gap-6 items-center">
              <div class="col-span-12">
                <div class="swiper cart-swiper mt-2 bg-slate-100 rounded-xl">
                  <div class="swiper-wrapper">
                    <div class="swiper-slide">
                      <div class="">
                        <img :src="productData.get_image" alt="" class="max-w-full h-full mx-auto">
                      </div>
                    </div>
                  </div>
                </div>
              </div><!-- end grid-cols -->
            </div><!-- end grid -->
          </div><!-- end grid-cols -->

          <div class="lg:col-span-6">
            <div class="pt-6">
              <div class="flex items-center gap-2 justify-between">
                <h3 class="mb-4 font-bold text-3xl text-gray-800">
                  {{ productData.name }}
                  <span
                      class="inline-flex items-center justify-center align-middle bg-orange-600/20 text-orange-500 py-1 px-2 mb-4 md:mb-0 rounded text-xs font-normal">In Stock</span>
                </h3>
              </div><!-- end heading -->
              <h4 class="mb-4 flex items-center gap-2 font-semibold">
                <span class="text-2xl text-green-700">₹{{ productData.price }}</span>
              </h4><!-- end rate -->
<!--              <div class="flex items-center gap-2 mb-2">-->
<!--                <div class="flex gap-1.5">-->
<!--                  <i data-lucide="star" class="w-5 h-5 fill-yellow-400 stroke-yellow-400"></i>-->
<!--                  <i data-lucide="star" class="w-5 h-5 fill-yellow-400 stroke-yellow-400"></i>-->
<!--                  <i data-lucide="star" class="w-5 h-5 fill-yellow-400 stroke-yellow-400"></i>-->
<!--                  <i data-lucide="star" class="w-5 h-5 fill-yellow-400 stroke-yellow-400"></i>-->
<!--                  <i data-lucide="star" class="w-5 h-5 fill-yellow-400 stroke-yellow-400"></i>-->
<!--                </div>-->
<!--                <h6 class="text-sm font-medium text-gray-500">(1.2k)</h6>-->
<!--              </div>-->

              <hr class="my-6 bg-gray-400">


              <div>
                <p class="text-base font-medium text-gray-500">
                  {{productData.description}}
                </p>
              </div><!-- end text -->

              <hr class="my-6 bg-gray-400">

              <div class="flex gap-2 items-center capitalize mt-3 w-full">
                <button
                    class="bg-primary text-white rounded-lg px-4 py-3 text-sm w-full font-medium flex justify-center items-center gap-x-2 transition transform ease-in-out hover:-translate-y-0.5"
                    @click="addToCart">
                  <i data-lucide="shopping-cart" class="h-4 w-4"></i> Add to cart
                </button>
                <div class="inline-flex justify-between border border-gray-300 p-1 rounded-full">
                  <button type="button"
                          class="minus flex-shrink-0 bg-slate-200 text-gray-800 rounded-full h-8 w-8 text-xl inline-flex items-center justify-center"
                          @click="this.quantity = this.quantity - 1">–
                  </button>
                  <input type="text" class="w-12 border-0 text-center focus:ring-0 p-0" min="0" max="100"
                         v-bind:value="quantity">
                  <button type="button"
                          class="plus flex-shrink-0 bg-slate-200 text-gray-800 rounded-full h-8 w-8 text-xl inline-flex items-center justify-center"
                          @click="this.quantity = this.quantity + 1">+
                  </button>
                </div>
                <a href="#">
                  <i data-lucide="heart" class="text-gray-600 hover:text-red-500 hover:fill-red-500"></i>
                </a>
              </div><!-- end btn -->

              <hr class="my-6 bg-gray-400">

              <div class="">
                <h6 class="text-base text-gray-800 mb-2">
                  <span>Category : </span>
                  <span class="text-gray-400">{{ productData.get_category }}</span>
                </h6>

              </div><!-- end category && Tags -->
            </div>
          </div><!-- end grid-cols -->
        </div><!-- end grid -->
      </div><!-- end container -->

      <hr class="my-16">

      <section class="">
        <div class="container">
          <div class="lg:border-b border-gray-300 mb-10 lg:flex justify-between items-center">
            <h1 class="inline-block text-2xl font-semibold text-gray-800 pb-4 border-b-4 border-primary -mb-px">Review &
              Information</h1>
            <nav class="-mb-1 flex  lg:gap-x-6 gap-x-1.5 lg:mt-0 mt-4 lg:w-auto w-[95%] lg:pb-0 pb-3 overflow-x-auto"
                 aria-label="Tabs" role="tablist">
              <button type="button"
                      class="hs-tab-active:border-primary hs-tab-active:text-primary flex-1 py-2.5 px-4 inline-flex items-center justify-center gap-2 border-b-[3px] border-transparent lg:text-base text-sm  whitespace-nowrap text-gray-800 hover:text-primary active"
                      id="descriptions-item" data-hs-tab="#descriptions" aria-controls="descriptions" role="tab">
                Descriptions
              </button>
              <button type="button"
                      class="hs-tab-active:border-primary hs-tab-active:text-primary flex-1 py-2.5 px-4 inline-flex items-center justify-center gap-2 border-b-[3px] border-transparent lg:text-base text-sm  whitespace-nowrap text-gray-800 hover:text-primary"
                      id="additional-information-item" data-hs-tab="#additional-information"
                      aria-controls="additional-information" role="tab">
                Additional Information
              </button>
              <button type="button"
                      class="hs-tab-active:border-primary hs-tab-active:text-primary flex-1 py-2.5 px-4 inline-flex items-center justify-center gap-2 border-b-[3px] border-transparent lg:text-base text-sm  whitespace-nowrap text-gray-800 hover:text-primary"
                      id="customer-feedback-item" data-hs-tab="#customer-feedback" aria-controls="product-details-tab"
                      role="tab">
                Customer Feedback
              </button>
            </nav><!-- end nav -->
          </div>

          <div>
            <div id="descriptions" role="tabpanel" aria-labelledby="descriptions-item">
              <div class="grid lg:grid-cols-2 gap-6">
                <div>
                  <img src="@/assets/images/bg/couple.png" alt="" class="mb-6 w-full">
                  <div class="border rounded-lg p-6">
                    <div class="grid grid-cols-2">
                      <div class="flex  items-center">
                        <i data-lucide="tag" class="text-primary w-8 h-8 me-4"></i>
                        <div class="">
                          <h6 class="text-base font-semibold text-gray-800 mb-2">50% Discount</h6>
                          <p>Save your 50% money with us</p>
                        </div>
                      </div>
                      <div class="flex items-center">
                        <i data-lucide="hop-off" class="text-primary w-8 h-8 me-4"></i>
                        <div class="">
                          <h6 class="text-base font-semibold text-gray-800">100% Organic</h6>
                          <p>100% Organic Vegetables</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div><!-- end grid-cols -->

                <div>
                  <p class="text-base text-gray-500 mb-10">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                    exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
                    reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
                    occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum sed
                    ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam
                    rem aperiam.</p>
                  <p class="text-base text-gray-500 mb-10">At vero eos et accusamus et iusto odio dignissimos ducimus
                    qui blanditiis praesentium volupthum deleniti atque corrupti quos dolores et quas molestias
                    excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt
                    mollitia animi</p>

                  <div class="space-y-4 mb-10">
                    <div class="flex items-center gap-2">
                  <span class="inline-flex items-center justify-center bg-primary text-white rounded-full h-6 w-6">
                    <i data-lucide="check" class="h-5 w-5"></i>
                  </span>
                      <p class="text-base">100 g of fresh leaves provides.</p>
                    </div>
                    <div class="flex items-center gap-2">
                  <span class="inline-flex items-center justify-center bg-primary text-white rounded-full h-6 w-6">
                    <i data-lucide="check" class="h-5 w-5"></i>
                  </span>
                      <p class="text-base">Aliquam ac est at augue volutpat elementum.</p>
                    </div>
                    <div class="flex items-center gap-2">
                  <span class="inline-flex items-center justify-center bg-primary text-white rounded-full h-6 w-6">
                    <i data-lucide="check" class="h-5 w-5"></i>
                  </span>
                      <p class="text-base">Quisque nec enim eget sapien molestie.</p>
                    </div>
                    <div class="flex items-center gap-2">
                  <span class="inline-flex items-center justify-center bg-primary text-white rounded-full h-6 w-6">
                    <i data-lucide="check" class="h-5 w-5"></i>
                  </span>
                      <p class="text-base">Proin convallis odio volutpat finibus posuere.</p>
                    </div>
                  </div>

                  <p class="text-base text-gray-500 mb-10">Cras et diam maximus, accumsan sapien et, sollicitudin velit.
                    Nulla blandit eros non turpis lobortis iaculis at ut Lorem ipsum dolor sit amet, consectetur
                    adipiscing elit, sed do eiusmod tempor incididunt ut labore ullamco laboris nisi ut aliquip.</p>
                </div><!-- end grid-cols -->
              </div><!-- end grid -->
            </div><!-- end descriptions -->

            <div id="additional-information" class="hidden" role="tabpanel"
                 aria-labelledby="additional-information-item">
              <div class="grid lg:grid-cols-2 gap-6">
                <div>
                  <img src="@/assets/images/bg/couple.png" alt="" class="mb-6 w-full">
                  <div class="border rounded-lg p-6">
                    <div class="grid grid-cols-2">
                      <div class="flex  items-center">
                        <i data-lucide="tag" class="text-primary w-8 h-8 me-4"></i>
                        <div class="">
                          <h6 class="text-base font-semibold text-gray-800 mb-2">50% Discount</h6>
                          <p>Save your 50% money with us</p>
                        </div>
                      </div><!-- end grid-cols -->

                      <div class="flex items-center">
                        <i data-lucide="hop-off" class="text-primary w-8 h-8 me-4"></i>
                        <div class="">
                          <h6 class="text-base font-semibold text-gray-800">100% Organic</h6>
                          <p>100% Organic Vegetables</p>
                        </div>
                      </div><!-- end grid-cols -->
                    </div><!-- end grid -->
                  </div>
                </div><!-- end grid-cols -->

                <div>
                  <table class="w-full">
                    <tbody class="">
                    <tr>
                      <td class="text-base text-gray-700 font-semibold py-2 w-36">Weight :</td>
                      <td class="text-base text-gray-500 py-2">03</td>
                    </tr>
                    <tr>
                      <td class="text-base text-gray-700 font-semibold py-2 w-36">Color :</td>
                      <td class="text-base text-gray-500 py-2">Green</td>
                    </tr>
                    <tr>
                      <td class="text-base text-gray-700 font-semibold py-2 w-36">Type :</td>
                      <td class="text-base text-gray-500 py-2">Organic</td>
                    </tr>
                    <tr>
                      <td class="text-base text-gray-700 font-semibold py-2 w-36">Category :</td>
                      <td class="text-base text-gray-500 py-2">Vegetables</td>
                    </tr>
                    <tr>
                      <td class="text-base text-gray-700 font-semibold py-2 w-36">Stock Status :</td>
                      <td class="text-base text-gray-500 py-2">Available</td>
                    </tr>
                    <tr>
                      <td class="text-base text-gray-700 font-semibold py-2 w-36">Tags :</td>
                      <td class="text-base text-gray-500 py-2">Vegetables, Healthy, Cabbage, Green Cabbage, Food,
                        Salad
                      </td>
                    </tr>
                    <tr>
                      <td class="text-base text-gray-700 font-semibold py-2 w-36">SKU :</td>
                      <td class="text-base text-gray-500 py-2">FWG15VFK</td>
                    </tr>
                    <tr>
                      <td class="text-base text-gray-700 font-semibold py-2 w-36">MFG :</td>
                      <td class="text-base text-gray-500 py-2">23 March, 2023</td>
                    </tr>
                    <tr>
                      <td class="text-base text-gray-700 font-semibold py-2 w-36">Stock Items :</td>
                      <td class="text-base text-gray-500 py-2">15 Items in Stock</td>
                    </tr>
                    </tbody>
                  </table>
                </div><!-- end grid-cols -->
              </div><!-- end grid -->
            </div><!-- end additional-information -->

            <div id="customer-feedback" class="hidden" role="tabpanel" aria-labelledby="customer-feedback-item">
              <div class="grid lg:grid-cols-12 gap-10">
                <div class="lg:col-span-8">
                  <div class="flex flex-col divide-y divide-gray-300">
                    <div class="">
                      <div class="inline-flex items-center gap-4 mb-4">
                        <img src="@/assets/images/avatars/img-1.jpg" alt="" class="h-10 w-10 rounded-full">
                        <div class="">
                          <h6 class="text-base font-medium text-gray-700 mb-0.5">Kianna Levin</h6>
                          <div class="flex items-center gap-2">
                            <div class="flex gap-1">
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                            </div>
                            <h6 class="text-sm font-medium text-gray-500">(1.2k)</h6>
                          </div>
                        </div>
                      </div>
                      <p class="text-base float-right mt-0.5">2 min ago</p>
                      <p class="text-base text-gray-600 mb-6">Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                        sed do eiusmod tempor</p>
                    </div><!-- end card -->
                    <div class="pt-6">
                      <div class="inline-flex items-center gap-4 mb-4">
                        <img src="@/assets/images/avatars/img-2.jpg" alt="" class="h-10 w-10 rounded-full">
                        <div class="">
                          <h6 class="text-base font-medium text-gray-700 mb-0.5">Haylie Levin</h6>
                          <div class="flex items-center gap-2">
                            <div class="flex gap-1">
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-slate-200 stroke-slate-200"></i>
                            </div>
                            <h6 class="text-sm font-medium text-gray-500">(600)</h6>
                          </div>
                        </div>
                      </div>
                      <p class="text-base float-right mt-0.5">30 Apr, 2021</p>
                      <p class="text-base text-gray-600 mb-6">Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
                        nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
                        dolor in reprehenderit in voluptate</p>
                    </div><!-- end card -->
                    <div class="pt-6">
                      <div class="inline-flex items-center gap-4 mb-4">
                        <img src="@/assets/images/avatars/img-3.jpg" alt="" class="h-10 w-10 rounded-full">
                        <div class="">
                          <h6 class="text-base font-medium text-gray-700 mb-0.5">Ryan Rosser</h6>
                          <div class="flex items-center gap-2">
                            <div class="flex gap-1">
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                            </div>
                            <h6 class="text-sm font-medium text-gray-500">(1.8k)</h6>
                          </div>
                        </div>
                      </div>
                      <p class="text-base float-right mt-0.5">22 Apr, 2021</p>
                      <p class="text-base text-gray-600 mb-6">"Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
                        nostrud exercitation ullamco</p>
                    </div><!-- end card -->
                    <div class="pt-6">
                      <div class="inline-flex items-center gap-4 mb-4">
                        <img src="@/assets/images/avatars/img-4.jpg" alt="" class="h-10 w-10 rounded-full">
                        <div class="">
                          <h6 class="text-base font-medium text-gray-700 mb-0.5">James Arcand</h6>
                          <div class="flex items-center gap-2">
                            <div class="flex gap-1">
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                              <i data-lucide="star" class="w-4 h-4 fill-yellow-400 stroke-yellow-400"></i>
                            </div>
                            <h6 class="text-sm font-medium text-gray-500">(1.2k)</h6>
                          </div>
                        </div>
                      </div>
                      <p class="text-base float-right mt-0.5">14 Apr, 2021</p>
                      <p class="text-base text-gray-600 mb-6">Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                        sed do eiusmod tempor</p>
                    </div><!-- end card -->
                  </div><!-- end flex -->
                </div><!-- end grid-cols -->
                <div class="lg:col-span-4">
                  <h3 class="text-xl font-semibold text-gray-700 mb-2">Be the first review on “Fresh Lettuce”</h3>
                  <p class="text-base mb-4">Your email address will not be published, Required fields are marked*</p>

                  <div class="flex items-center gap-2 mb-10">
                    <h4 class="text-lg font-medium text-gray-800">Your Rating <span class="text-red-500">*</span></h4>
                    <div class="flex gap-1.5">
                      <i data-lucide="star"
                         class="w-5 h-5 text-slate-400 hover:fill-yellow-400 hover:text-yellow-400 focus:fill-yellow-400 focus:text-yellow-400"></i>
                      <i data-lucide="star"
                         class="w-5 h-5 text-slate-400 hover:fill-yellow-400 hover:text-yellow-400 focus:fill-yellow-400 focus:text-yellow-400"></i>
                      <i data-lucide="star"
                         class="w-5 h-5 text-slate-400 hover:fill-yellow-400 hover:text-yellow-400 focus:fill-yellow-400 focus:text-yellow-400"></i>
                      <i data-lucide="star"
                         class="w-5 h-5 text-slate-400 hover:fill-yellow-400 hover:text-yellow-400 focus:fill-yellow-400 focus:text-yellow-400"></i>
                      <i data-lucide="star"
                         class="w-5 h-5 text-slate-400 hover:fill-yellow-400 hover:text-yellow-400 focus:fill-yellow-400 focus:text-yellow-400"></i>
                    </div>
                  </div>

                  <form action="">
                    <div class="grid md:grid-cols-12 gap-6">
                      <div class="md:col-span-6">
                        <label for="name" class="mb-2.5 block text-sm font-medium text-gray-700">Name <span
                            class="text-red-500">*</span></label>
                        <input type="text" id="name"
                               class="py-2.5 text-sm block w-full rounded border-gray-300 focus:ring-0 focus:border-primary"/>
                      </div>
                      <div class="md:col-span-6">
                        <label for="e_mail" class="mb-2.5 block text-sm font-medium text-gray-700">Email <span
                            class="text-red-500">*</span></label>
                        <input type="text" id="e_mail"
                               class="py-2.5 text-sm block w-full rounded border-gray-300 focus:ring-0 focus:border-primary"/>
                      </div>
                      <div class="md:col-span-12">
                        <label for="e_mail" class="mb-2.5 block text-sm font-medium text-gray-700">Your Review <span
                            class="text-red-500">*</span></label>
                        <input type="email" id="e_mail"
                               class="py-2.5 text-sm block w-full rounded border-gray-300 focus:ring-0 focus:border-primary"/>
                      </div>
                      <div class="md:col-span-12">
                        <div class="flex items-center gap-2 mb-6">
                          <input type="checkbox"
                                 class="shrink-0 mt-0.5 border-gray-200 rounded text-primary pointer-events-none focus:ring-primary"
                                 id="comment">
                          <label for="comment" class="text-sm text-gray-500">Save name, Email in this browser for the
                            comment</label>
                        </div>
                        <a href="#"
                           class="rounded border border-primary bg-primary px-6 py-2.5 text-center text-sm font-medium text-white shadow-sm transition-all">Submit</a>
                      </div>
                    </div>
                  </form>
                </div><!-- end grid-cols -->
              </div><!-- end grid -->
            </div><!-- end customer-feedback -->
          </div>
        </div><!-- end container -->
      </section>

    </section>
  </Layout>
</template>

<script lang="ts">
import Layout from "@/components/layouts/layout.vue";
import axios from "axios";
import {useEcomStore} from "@/stores";

export default {
  components: {Layout},
  data() {
    return {
      productData: {},
      useEcom: useEcomStore(),
      quantity: 1,
      isAdded: false
    };
  },

  mounted() {
    this.getProduct()
  },
  methods: {
    async getProduct() {
      this.useEcom.setIsLoading(true)
      const category_slug = this.$route.params.category_slug
      const product_slug = this.$route.params.product_slug

      await axios.get(`/api/products/${category_slug}/${product_slug}`).then(res => this.productData = res.data)

      this.useEcom.setIsLoading(false)
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1
      }

      const item = {
        product: this.productData,
        quantity: this.quantity
      }

      this.useEcom.addToCart(item)
      this.isAdded = true

      setTimeout(() => {
        this.isAdded = false
      }, 3000)
    }
  }
}
</script>
