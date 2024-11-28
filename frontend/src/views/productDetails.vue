<script setup>
import navigation from "@/components/navigation.vue";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const product = ref([]);

async function getProductDetails() {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/productList/${route.params.id}/`,
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    product.value = response.data;
    console.log("Product details:", productDetails.value);
  } catch (error) {
    console.error("Error fetching product details:", error);
  }
}

onMounted(() => {
  getProductDetails();
});
</script>

<template>
  <navigation />

  <section class="product">
    <div class="porduct_images">
      <img :src="product.productImage" alt="" />
    </div>
    <div class="product_main">
      <div class="product_details">
        <h4 class="product_name">
          {{ product.productName }}
        </h4>
        <div class="product_total">
          <p class="product_number">1</p>
          <p class="product_price">{{ product.productPrice }} frw</p>
        </div>
        <button class="product_add">add to cart</button>
      </div>
      <div class="about">
        <h4 class="about_title">about taakarwanda</h4>

        <img
          class="about_img"
          src="../assets/photography/placeholder.jpg"
          alt=""
        />
        <p class="about_desc">
          taakarwanda is a platform that was build with the idea of helping
          rwandan artists gain expose and reach an audience with their workin
          addition to taakarwanda is a platform that was build with
        </p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.product {
  height: calc(100vh - 80px);
  margin-top: 80px;
  padding: 8px 144px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;

  .porduct_images {
    width: 50vw;
    height: 100%;

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border: 1px solid rgb(21, 0, 254);
    }
  }

  .product_main {
    width: 50vw;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;

    .product_details {
      width: 440px;
      display: flex;
      flex-direction: column;
      gap: 16px;

      .product_name {
        font-size: 24px;
        font-weight: 700;
        text-transform: uppercase;
      }

      .product_total {
        display: flex;
        justify-content: space-between;
        padding: 16px;
        border: 1.4px solid rgb(21, 0, 254);
        border-radius: 4px;
        text-transform: lowercase;
        color: rgb(21, 0, 254);

        p {
          font-size: 20px;
        }
      }

      .product_add {
        border: none;
        background-color: rgb(17, 0, 203);
        color: white;
        font-size: 16px;
        padding: 24px;
        text-transform: uppercase;
        text-align: center;

        border-radius: 4px;
        cursor: pointer;
      }
    }

    .about {
      width: 440px;
      display: flex;
      flex-direction: column;
      gap: 8px;

      h4 {
        font-size: 20px;
      }

      img {
        object-fit: cover;
        border: 1px solid rgb(21, 0, 254);
        border-radius: 4px;
      }
      .about_desc {
        font-size: 16px;
      }
    }
  }
}
</style>
