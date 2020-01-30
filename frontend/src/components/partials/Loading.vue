<template>
    <div class='loading' :class='{ "is-hidden": hidden }'></div>
</template>

<script>
import { EventBus } from '../eventBus'

export default {
    data: function () {
        return {
            hidden: true,
        }
    },
    mounted () {
        EventBus.$on('loading:start', () => {
            this.hidden = false
        })
        EventBus.$on('loading:end', () => {
            this.hidden = true
        })
    }
}
</script>

<style scoped lang='scss' src='@/scss/partials/loading.scss'></style>
