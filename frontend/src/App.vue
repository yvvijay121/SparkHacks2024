<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <!-- <header>

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header> -->
  <nav class="navbar is-fixed-top is-transparent">
    <div class="container is-fluid force-full">
      <nav class="level is-mobile mx-5">
        <div class="level-left">
          <div class="level-item has-text-centered">
            <RouterLink to="/home"><span class="tag is-info is-large has-text-weight-bold box"><ion-icon name="shield-outline"
                  class="pr-2"></ion-icon>aegisRx</span></RouterLink>
          </div>
        </div>
        <div class="level-right">
          <div class="level-item has-text-centered">
            <router-link to="/user_select" custom v-slot="{ navigate }">
              <button class="button is-small box" @click="navigate">
                <span class="icon is-small">
                  <ion-icon name="people-circle-outline"></ion-icon>
                </span>
              </button>
            </router-link>
          </div>
        </div>
      </nav>
    </div>
  </nav>
  <div class="container is-fluid mt-6 mb-7">
    <RouterView/>
  </div>
  <nav class="navbar is-fixed-bottom is-transparent">
    <div class="container is-fluid force-full">
      <nav class="level is-mobile mx-5">
        <div class="level-item has-text-centered">
          <router-link to="/med_line" custom v-slot = "{ navigate }">
            <button class="button is-large box" @click = "navigate">
              <span class="icon is-small">
                <ion-icon name="search-outline"></ion-icon>
              </span>
            </button>
          </router-link>
        </div>
        <div class="level-item has-text-centered">
          <router-link to="/drug_list" custom v-slot="{ navigate }">
              <button class="button is-large box" @click="navigate">
                <span class="icon is-small">
              <ion-icon name="list-outline"></ion-icon>
            </span>
              </button>
            </router-link>
        </div>
      </nav>
    </div>
  </nav>
</template>

<style>
@import '../node_modules/bulma/css/bulma.css';

.force-full {
  display: inline !important;
}

.mb-7 {
  margin-bottom: 5rem;
}
</style>
