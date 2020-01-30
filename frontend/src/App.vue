<template>
    <div id='app'>
        <Loading />
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
import Loading from './components/partials/Loading'

export default {
    name: 'app',
    components: {
        Navigation,
        Loading,
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
