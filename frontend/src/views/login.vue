<script setup>
import navigation from "@/components/navigation.vue";
import { useUserAuthStore } from "@/scripts/userauth";
import { useRouter } from "vue-router";
import { reactive } from "vue";

const router = useRouter();
const UserAuthStore = useUserAuthStore();
const form = reactive({
  email: "",
  password: "",
});
async function authLogin() {
  const authLogin = await UserAuthStore.authLogin(form.email, form.password);

  if (authLogin) {
    router.push("/create");
  }
}
</script>

<template>
  <navigation />
  <section class="account">
    <h4>welcome back</h4>
    <div class="account-create">
      <form class="account-create-form" @submit.prevent="authLogin">
        <input
          v-model="form.email"
          type="email"
          name="email"
          id="email"
          placeholder="email"
          required
        />

        <input
          v-model="form.password"
          type="password"
          name="password"
          id="password"
          placeholder="password"
          required
        />

        <input type="submit" required value="log in" class="form-cta" />
      </form>
    </div>

    <div class="or-title">
      <div class="or-divide"></div>
      <p>or</p>
      <div class="or-divide"></div>
    </div>
    <div class="create-account">
      <p>don't have an account yet ?</p>
      <router-link to="/account/register">create account</router-link>
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
    font-size: 32px;
    text-transform: capitalize;
    font-family: cardinal-fruit;
  }

  .account-create {
    width: 32vw;
    display: flex;
    flex-direction: column;
    gap: 32px;

    .account-create-form {
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
    width: 32vw;
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
    width: 32vw;
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
