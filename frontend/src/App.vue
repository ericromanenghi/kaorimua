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
    },
    watch: {
        '$route': {
            handler (to) {
                const defaultTitle = 'Kaori MUA'
                document.title = (to.meta && to.meta.title) ? `${to.meta.title} | ${defaultTitle}` : defaultTitle
            },
            immediate: true,
        }
    }
}
</script>
