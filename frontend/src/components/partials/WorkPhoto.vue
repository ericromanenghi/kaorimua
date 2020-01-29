<template>
    <div class='photo' :style='{ width: width, backgroundImage: `url(${photo.src})` }'></div>
</template>

<script>
export default {
    props: [ 'photo' ],
    data: function () {
        return {
            width: '0px',
        }
    },
    methods: {
        calculateWidth () {
            return `${this.photo.ratio / 100 * this.$el.clientHeight}px`
        },
        resize () {
            this.width = this.calculateWidth()
        }
    },
    mounted () {
        this.resize()
        window.addEventListener('resize', this.resize)
    },
    destroyed () {
        window.removeEventListener('resize', this.resize)
    }
}
</script>

<style lang='scss' src='@/scss/photo.scss' scoped></style>
