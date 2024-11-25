<script setup>
import card from "@/components/card.vue";
import navigation from "@/components/navigation.vue";
import contact from "@/components/contact.vue";
</script>

<template>
  <navigation />
  <section class="se-hero">
    <div class="hero-main">
      <h1>ni taakarwanda</h1>
      <p>redefining the aesthetics of interiors</p>
      <RouterLink to="/shop" class="hero-cta"> start shopping </RouterLink>
    </div>
    <div class="hero-imgs-wrapper">
      <div class="hero-img hero-img-1">
        <img src="../assets/photography/hero-1-modified.jpg" alt="" />
      </div>
      <div class="hero-img hero-img-2">
        <img src="../assets/photography/hero-2-modified.jpg" alt="" />
      </div>
      <div class="hero-img hero-img-3">
        <img src="../assets/photography/hero-3-modified.webp" alt="" />
      </div>
    </div>
  </section>

  <!--  -->
  <section class="se-about">
    <p class="about-par">
      taakarwanda is a rwandan based platform<br />
      designed to elevate artist through<br />
      exposure of their work to the world<br />
    </p>
    <RouterLink to="/about" class="about-cta">learn more</RouterLink>
  </section>

  <!--  -->
  <div class="inspired-img">
    <img src="../assets/photography/bigimg.webp" alt="" />
  </div>

  <!--  -->
  <section class="se-mission">
    <div class="mission-01">
      <h4 class="mission-title-01">art related,</h4>
      <h4 class="mission-title-02">sell and buy.</h4>
      <img
        src="../assets/photography/set-2.jpg"
        alt=""
        class="mission-01-img"
      />
    </div>
    <div class="mission-02">
      <h4 class="mission-title-03">art related,</h4>
      <h4 class="mission-title-04">sell and buy.</h4>
    </div>
    <div class="mission-03">
      <img
        src="../assets/photography/set-1.jpg"
        alt=""
        class="mission-02-img"
      />
      <p class="about-main-p">
        why, send on art ? well Owning a piece of art is a powerful way to
        express your personality in the spaces where you live,work, and dine.
        Art breathes life into your surroundings, making each space uniquely
        yours.
        <br />
        <br />
        so Don’t do let your space be average like the rest grb your self a
        piece or two
      </p>
    </div>
  </section>

  <section class="how-it-works">
    <p>
      why, send on art ? well Owning a piece of art is a powerful<br />
      way to express your personality in the spaces
    </p>
  </section>

  <!--  -->
  <section class="process">
    <div class="process-cards">
      <card class="card-01">
        <template #card-title>
          <h4>
            signup at<br />
            taakrwanda
          </h4>
        </template>
        <template #card-title-num>
          <h4>01.</h4>
        </template>

        <template #card-desc>
          <p>
            how does an artists get started with<br />
            taakarwanda to host their work
          </p>
        </template>

        <img class="card-img" src="../assets/photography/upload.jpg" alt="" />
      </card>
      <card class="card-02">
        <template #card-title>
          <h4>
            upload<br />
            your work
          </h4>
        </template>
        <template #card-title-num>
          <h4>02.</h4>
        </template>

        <template #card-desc>
          <p>
            how does an artists get started with<br />
            taakarwanda to host their work
          </p>
        </template>

        <img class="card-img" src="../assets/photography/audience.jpg" alt="" />
      </card>
      <card class="card-03">
        <template #card-title>
          <h4>
            reach<br />
            audience
          </h4>
        </template>
        <template #card-title-num>
          <h4>03.</h4>
        </template>

        <template #card-desc>
          <p>
            how does an artists get started with<br />
            taakarwanda to host their work
          </p>
        </template>

        <img
          class="card-img"
          src="../assets/photography/audience-2.jpg"
          alt=""
        />
      </card>
      <card class="card-04">
        <template #card-title>
          <h4>
            receive<br />
            payment
          </h4>
        </template>
        <template #card-title-num>
          <h4>04.</h4>
        </template>

        <template #card-desc>
          <p>
            how does an artists get started with<br />
            taakarwanda to host their work
          </p>
        </template>

        <img class="card-img" src="../assets/photography/payement.jpg" alt="" />
      </card>
    </div>
  </section>

  <!--  -->
  <section>
    <div class="se-start">
      <p>
        now that you have seen how it works<br />
        get started with taakarwanda and start <br />
        selling your work to the world
      </p>

      <RouterLink to="/account/login" class="start-cta">get started</RouterLink>
    </div>
  </section>
  <contact />
</template>

<style scoped>
@font-face {
  font-family: cardinal-fruit;
  src: url(../assets/fonts/CardinalFruit-Regular.woff2);
}
/*  */
.se-hero {
  margin-top: 60px;
  padding: 8px 144px;
  /*  */
  display: flex;
  flex-direction: column;
  gap: 8px;

  .hero-main {
    height: 65vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 24px;
    h1 {
      font-family: cardinal-fruit;
      font-size: 144px;
      line-height: 144px;
      color: #0722f6;
    }

    p {
      color: #0722f6;
      font-size: 18px;
      padding: 0 4px;
      background-color: #e9e3e9;
    }

    .hero-cta {
      font-size: 36px;
      line-height: 36px;
      text-transform: capitalize;
      padding: 8px 72px;
      border: 1.75px solid #0722f6;
      color: #0722f6;
      background-color: #e9e3e9;
      font-family: cardinal-fruit;
      cursor: pointer;
    }
  }

  .hero-imgs-wrapper {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    .hero-img {
      border: 2px solid #0722f6;
      width: 100%;
      position: relative;
      img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        position: absolute;
      }
    }

    .hero-img::after {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: black;
      opacity: 0.35;
      pointer-events: none;
    }

    .hero-img-1 {
      grid-column: 1/3;
      transform: rotate(-2.5deg);
      height: 640px;
    }

    .hero-img-2 {
      grid-column: 3/5;
      z-index: 100;
      width: 540px;
      height: 640px;
    }
    .hero-img-3 {
      grid-column: 5/-1;
      height: 640px;
      transform: rotate(4.5deg);
    }
  }
}

/*  */
.se-about {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 160px;

  .about-par {
    font-size: 72px;
    text-transform: lowercase;
    text-align: center;
    font-family: cardinal-fruit;
    color: #0722f6;
    /* color: #1500fe; */
  }

  .about-cta {
    font-size: 36px;
    text-transform: capitalize;
    padding: 8px 72px;
    border: 2px solid #0722f6;
    color: #0722f6;
    font-family: cardinal-fruit;
    cursor: pointer;
  }
}

/*  */
.inspired-img {
  margin: 8px 144px;
  height: 100vh;
  border: 1px solid rgb(17, 0, 203);
  position: relative;

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
}

.inspired-img::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: black;
  opacity: 0.5;
  pointer-events: none;
}

/*  */
.se-mission {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 8px;
  padding: 200px 144px;
  height: 110vh;

  .mission-01 {
    grid-column: 1/4;
    display: flex;
    flex-direction: column;

    .mission-01-img {
      width: 320px;
      object-fit: cover;
      height: 256px;
      border: 1px solid #0722f6;
    }
  }

  .mission-02 {
    grid-column: 5/9;
    .mission-02-img {
      width: 320px;
      object-fit: cover;
      height: 256px;
      border: 1px solid #0722f6;
    }
  }

  .mission-03 {
    grid-column: 9/-1;
    display: flex;
    flex-direction: column;
    gap: 16px;
    .mission-03-img {
      width: 100%;
      object-fit: cover;
      height: 448px;
      border: 1px solid #0722f6;
    }

    p {
      font-size: 18px;
    }
  }
}

.how-it-works {
  height: 55vh;
  display: flex;
  justify-content: center;
  align-items: center;
  p {
    font-size: 22px;
    text-align: center;
  }
}

/*  */
.process {
  display: flex;
  height: 100vh;
  padding-top: 64px;
  /* background-color: rebeccapurple; */
  align-items: center;
  .process-cards {
    width: 100%;
    display: flex;
    justify-content: center;
    .card-01 {
      transform: rotate(2.5deg);
      margin-top: 24px;
      margin-right: -72px;
    }

    .card-02 {
      margin-right: -72px;
      transform: rotate(-3.5deg);
    }
    .card-03 {
      margin-right: -72px;
      transform: rotate(2.5deg);
      margin-top: 24px;
    }
    .card-04 {
      /* margin-right: -72px; */
      transform: rotate(3deg);
    }
  }
}

.se-start {
  display: flex;
  flex-direction: column;
  height: 100vh;
  justify-content: center;
  align-items: center;
  gap: 160px;
  padding: 8px;

  p {
    font-size: 72px;
    text-transform: lowercase;
    text-align: center;
    font-family: cardinal-fruit;
    color: #0722f6;
  }

  .start-cta {
    font-size: 36px;
    text-transform: capitalize;
    padding: 8px 72px;
    border: 2px solid #0722f6;
    color: #0722f6;
    font-family: cardinal-fruit;
    cursor: pointer;
  }
}
</style>
