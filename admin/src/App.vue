<template>
    <div id="app">
        <top-nav-bar title="Kaori MUA - Admin"></top-nav-bar>
        <galleries-container></galleries-container>
    </div>
</template>

<script>
import TopNavBar from './components/TopNavBar.vue'
import GalleriesContainer from './components/GalleriesContainer.vue'

export default {
    name: 'app',
    components: {
        TopNavBar,
        GalleriesContainer
    }
}
</script>

<style>
</style>
