<script setup>
import navigation from "@/components/navigation.vue";
import contact from "@/components/contact.vue";
</script>

<template>
  <navigation />

  <section class="about">
    <div class="about-wrapper">
      <h3 class="about-title">about</h3>
      <p class="about-desc">
        taakarwanda is a platform that was build with the idea of helping
        rwandan artists gain expose and reach an audience with their workin
        addition to the original idea a market gap was noticed that there is a
        lack of solutions in home decor so we decided to make it also a market
        place for anyone looking to elevate the feel and look of their living
        space
        <br />
        <br />
        taakarwanda is a platform that was build with the idea of helping
        rwandan artists gain expose and reach an audience with their workin
        addition to the original idea a
      </p>
      <p class="about-desc">
        taakarwanda is a platform that was build with the idea
      </p>
    </div>
  </section>
  <contact />
</template>

<style scoped>
.about {
  padding: 8px 144px;
  height: 80vh;
  width: 100%;
  display: flex;
  align-items: center;
  /* justify-content: flex-end; */

  .about-wrapper {
    width: 45vw;
    display: flex;
    flex-direction: column;
    gap: 36px;

    .about-desc {
      font-size: 18px;
      text-transform: capitalize;
    }
  }
}

.journal {
  padding: 8px;
  display: flex;
  flex-direction: column;
  /* justify-content: flex-end; */
  align-items: flex-end;
  gap: 36px;

  .journal-title {
    width: 45vw;
  }

  .journal-wrapper {
    display: flex;
    gap: 8px;

    .journal-wpr {
      flex-grow: 1;

      img {
        flex-grow: 1;
        object-fit: cover;
        border: 1px solid black;
      }

      .joural-desc {
        flex-grow: 1;
        font-size: 13px;
        text-transform: uppercase;
      }

      .journal-wpr-01-img {
        height: 335px;
      }
      .journal-wpr-02-img {
        height: 504px;
      }

      .journal-wpr-03-img {
        height: 402px;
      }

      .journal-wpr-04-img {
        height: 297px;
      }
    }
  }
}
</style>
