<template>
    <div id='app'>
        <Navigation />
        <transition
            name='fade'
            mode='out-in'
        >
            <router-view></router-view>
        </transition>
    </div>
</template>

<script>
import Navigation from './components/partials/Navigation'

export default {
    name: 'app',
    components: {
        Navigation
    }
}
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.2s;
  transition-property: opacity;
  transition-timing-function: ease;
}

.fade-enter,
.fade-leave-active {
  opacity: 0
}
</style>
