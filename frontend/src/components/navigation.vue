<script setup></script>

<template>
  <section class="navigation">
    <div class="nav-offer">
      <p>free shipping on all products</p>
    </div>
    <nav class="nav">
      <div class="nav-links">
        <RouterLink class="nav-links-a" to="/">taakarwanda</RouterLink>
        <RouterLink class="nav-links-a" to="/about">about</RouterLink>
        <RouterLink class="nav-links-a" to="/shop">shop all</RouterLink>
        <RouterLink class="nav-links-a" to="/account/login">account</RouterLink>
      </div>
      <RouterLink class="nav-links-a" to="/cart">cart</RouterLink>
    </nav>
  </section>
</template>

<style scoped>
@font-face {
  font-family: cardinal-fruit;
  src: url(../assets/fonts/CardinalFruit-Regular.woff2);
}
.navigation {
  z-index: 10000;
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  .nav-offer {
    background-color: rgb(17, 0, 203);
    height: 30px;
    display: flex;
    justify-content: center;
    align-items: center;

    p {
      color: white;
      font-size: 12px;
      text-transform: uppercase;
      /* font-family: cardinal-fruit; */
    }
  }

  .nav {
    padding: 8px 144px;
    height: 42px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #e9e3e9;

    .nav-links-a {
      color: #0722f6;
      font-size: 24px;
      text-transform: capitalize;
      line-height: 1;
      font-family: cardinal-fruit;
      cursor: pointer;
    }

    .nav-links {
      display: flex;
      width: 32vw;
      justify-content: space-between;
    }
  }
}
</style>
