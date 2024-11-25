<script setup></script>

<template>
  <footer class="footer">
    <div class="footer-wrapper">
      <p class="footer-desc">
        for further enquirers for both artist looking to sell and buyers
        <br />
        interested art please reach us through our email or socials.<br />
        takarwanda @2024
      </p>
      <div class="footer-links">
        <a href="">instagram</a>
        <a href="">tiktok</a>
        <a href="">terms & conditions</a>
        <a href="">back on top</a>
      </div>
      <a href="" class="link-email"> taakarwanda@info.com </a>
    </div>
    <div class="footer-title">taakarwanda</div>
  </footer>
</template>

<style scoped>
@font-face {
  font-family: cardinal-fruit;
  src: url(../assets/fonts/CardinalFruit-Regular.woff2);
}
.footer {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  height: 100vh;
  background: #161616;
  color: #e9e3e9;
  .footer-wrapper {
    height: 100%;
    width: 45vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    /* align-items: center; */
    gap: 24px;

    p {
      font-size: 15px;
      text-transform: uppercase;
    }

    .link-email {
      padding: 4px 32px;
      border: 1px solid black;
      width: fit-content;
      font-size: 15px;
      text-transform: uppercase;
    }
    .footer-links {
      display: flex;
      gap: 48px;

      a {
        font-size: 15px;
        text-transform: uppercase;
      }
    }
  }

  .footer-title {
    text-transform: uppercase;
    font-size: 204px;
    height: 342px;
    overflow: hidden;
    /* display: block; */
    font-family: cardinal-fruit;
  }
}
</style>
