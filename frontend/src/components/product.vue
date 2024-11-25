<script setup></script>

<template>
  <div class="product-wrapper">
    <slot> </slot>
    <div class="product-details">
      <p class="productName">
        <slot name="productName"></slot>
      </p>

      <p class="productPrice">
        <slot name="productPrice"></slot>
      </p>
    </div>
  </div>
</template>

<style scoped>
.product-wrapper {
  border: 2px solid #0722f6;
  display: flex;
  flex-direction: column;
  gap: 8px;

  .product-details {
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding: 8px;

    .productName,
    .productPrice {
      font-size: 14px;
      text-transform: uppercase;
    }
  }
}
</style>
