<script setup>
import navigation from "@/components/navigation.vue";
import { useUserAuthStore } from "@/scripts/userauth";
import { useRouter } from "vue-router";
import { reactive } from "vue";

const router = useRouter();
const UserAuthStore = useUserAuthStore();
const form = reactive({
  fullNames: "",
  email: "",
  password: "",
});

async function authRegister() {
  try {
    await UserAuthStore.authRegister(form.fullNames, form.email, form.password);
    if (authRegister) {
      router.push("/account/login");
    }
  } catch (error) {
    console.error("Error registering:", error);
  }
}
</script>

<template>
  <navigation />
  <section class="account">
    <h4>new to taakarwanda</h4>
    <h4>Create an account to upload your art and reach the world</h4>
    <div class="account-create">
      <form
        action=""
        class="account-register-form"
        @submit.prevent="authRegister"
      >
        <input
          type="text"
          name="fullnames"
          id="fullnames"
          required
          placeholder="full names"
          v-model="form.fullNames"
        />
        <input
          type="email"
          name="email"
          id="email"
          required
          placeholder="email address"
          v-model="form.email"
        />
        <input
          type="password"
          name="password"
          id="password"
          placeholder="choose password"
          required
          v-model="form.password"
        />
        <input type="submit" required value="create account" class="form-cta" />
      </form>
    </div>
  </section>
</template>

<style scoped>
@font-face {
  font-family: cardinal-fruit;
  src: url(../assets/fonts/CardinalFruit-Regular.woff2);
}
.account {
  height: calc(100vh - 64px);
  margin-top: 64px;
  padding: 8px 144px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  /* align-items: center; */
  gap: 32px;

  h4 {
    /* width: 40vw; */
    /* text-align: center; */
    font-size: 16px;
    /* align-self: center; */
    text-transform: capitalize;
    /* font-family: cardinal-fruit; */
  }
  .account-create {
    display: flex;
    flex-direction: column;
    width: 32vw;

    .account-register-form {
      display: flex;
      flex-direction: column;
      gap: 16px;

      input {
        padding: 24px;
        border: 1.4px solid rgb(17, 0, 203);
        font-size: 16px;
        border-radius: 4px;
        text-transform: capitalize;
        color: rgb(17, 0, 203);
      }

      .form-cta {
        border: none;
        background-color: rgb(17, 0, 203);
        color: white;
        font-size: 16px;
        padding: 24px;
        text-transform: uppercase;
        text-align: center;
        cursor: pointer;
      }
    }
  }

  .or-title {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    width: 40vw;
    .or-divide {
      height: 0.25px;
      background-color: rgb(17, 0, 203, 0.5);
      flex-grow: 1;
    }

    p {
      font-size: 18px;
      z-index: 100;
      color: rgb(17, 0, 203, 0.5);
    }
  }

  .create-account {
    width: 40vw;
    display: flex;
    justify-content: space-between;

    p {
      font-size: 18px;
    }

    a {
      border-bottom: 1px solid rgb(17, 0, 203);
      font-size: 18px;
      cursor: pointer;
    }
  }
}
</style>
