<script setup>
import navigation from "@/components/navigation.vue";
import contact from "@/components/contact.vue";
import product from "@/components/product.vue";
// import api from "../scripts/axios";
import axios from "axios";
import { onMounted, ref } from "vue";

const productList = ref([]);

async function getProductList() {
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/productList/", {
      headers: {
        "Content-Type": "application/json",
      },
    });
    productList.value = response.data;
  } catch (error) {
    console.error("Error fetching products:", error);
  }
}

onMounted(() => {
  getProductList();
});
</script>

<template>
  <navigation />
  <section class="se-shop">
    <div class="se-shop-about">
      <p class="se-shop-about-p">
        taakarwanda is a platform that was build with the idea of helping
        rwandan artists gain expose and reach an audience with their workin
        addition to the original idea
      </p>
    </div>

    <div class="shop-items-all">
      <product
        v-for="product in productList"
        :key="product.id"
        class="product-wrapper"
      >
        <img
          class="product-img"
          :src="product.productImage"
          alt="product.name"
        />
        <template #productName>{{ product.productName }}</template>
        <template #productPrice>from {{ product.productPrice }} frw</template>
      </product>
    </div>
  </section>
  <contact />
</template>

<style scoped>
.se-shop {
  /* height: calc(100vh - 60px); */
  margin-top: 96px;
  padding: 8px 144px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  .se-shop-about {
    width: 40vw;
    height: 25vh;
    /* align-self: flex-end; */

    .se-shop-about-p {
      font-size: 18px;
    }
  }

  .shop-items-all {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    flex-wrap: wrap;
    gap: 8px;

    .product-wrapper {
      grid-column: span 3;
      cursor: pointer;

      .product-img {
        width: 100%;
        height: 378px;
        flex-grow: 1;
        object-fit: cover;
      }
    }
  }
}
</style>
