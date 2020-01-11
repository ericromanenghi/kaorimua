<template>
    <div id='app'>
        <Navigation />
        <router-view></router-view>
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
</style>
