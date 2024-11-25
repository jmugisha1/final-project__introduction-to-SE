<script setup></script>

<template>
  <div class="process-card">
    <h4 class="card-title">
      <slot name="card-title"></slot>
    </h4>

    <h4 class="card-title-num">
      <slot name="card-title-num"></slot>
    </h4>

    <p class="card-desc">
      <slot name="card-desc"></slot>
    </p>

    <slot></slot>
  </div>
</template>

<style scoped>
.process-card {
  width: 440px;
  height: 520px;
  border: 1px solid #000;
  background-color: #fffffe;

  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 8px;

  .card-title,
  .card-title-num {
    font-size: 48px;
    text-transform: uppercase;
    font-weight: bold;
    text-align: center;
  }

  .card-desc {
    text-align: center;
    font-size: 16px;
  }
  ::v-deep .card-img {
    object-fit: cover;
    height: 24px;
    width: 100%;
  }
}
</style>
