<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
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
            <button class="button is-small">
              <span class="icon is-small">
                <ion-icon name="accessibility-outline"></ion-icon>
              </span>
            </button>
          </div>
        </div>
        <div class="level-right">
          <div class="level-item has-text-centered">
            <button class="button is-small">
              <span class="icon is-small">
                <ion-icon name="accessibility-outline"></ion-icon>
              </span>
            </button>
          </div>
        </div>
      </nav>
    </div>
  </nav>
  <div class="container is-fluid mt-6 mb-6">
    <RouterView />
  </div>
  <nav class="navbar is-fixed-bottom is-transparent">
    <div class="container is-fluid force-full">
      <nav class="level is-mobile mx-5">
        <div class="level-item has-text-centered">
          <button class="button is-large">
            <span class="icon is-small">
              <ion-icon name="accessibility-outline"></ion-icon>
            </span>
          </button>
        </div>
        <div class="level-item has-text-centered">
          <button class="button is-large">
            <span class="icon is-small">
              <ion-icon name="accessibility-outline"></ion-icon>
            </span>
          </button>
        </div>
        <div class="level-item has-text-centered">
          <button class="button is-large">
            <span class="icon is-small">
              <ion-icon name="accessibility-outline"></ion-icon>
            </span>
          </button>
        </div>
        <div class="level-item has-text-centered">
          <button class="button is-large">
            <span class="icon is-small">
              <ion-icon name="accessibility-outline"></ion-icon>
            </span>
          </button>
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
</style>
