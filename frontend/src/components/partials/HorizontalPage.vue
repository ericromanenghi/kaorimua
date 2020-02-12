<template>
    <div>
        <div class='work'>
            <div class='work__list' ref='container'>
                <slot></slot>
            </div>
        </div>
        <div class='arrows' v-show='showArrows'>
            <button class='arrow arrow--next' @click='scroll(1)' v-show='showNextArrow' aria-label='Next photo'>
                <svg xmlns='http://www.w3.org/2000/svg' width='19.59' height='13.821' viewBox='0 0 19.59 13.821'><g transform='translate(-38.5 -34.086)'><line x2='17.176' transform='translate(39.5 40.996)'/><line x2='5.496' y2='5.496' transform='translate(51.18 35.5)'/><line x1='5.496' y2='5.496' transform='translate(51.18 40.996)'/></g></svg>
            </button>
            <button class='arrow arrow--prev' @click='scroll(-1)' v-show='showPrevArrow' aria-label='Previous photo'>
                <svg xmlns='http://www.w3.org/2000/svg' width='19.59' height='13.821' viewBox='0 0 19.59 13.821'><g transform='translate(-38.5 -34.086)'><line x2='17.176' transform='translate(39.5 40.996)'/><line x2='5.496' y2='5.496' transform='translate(51.18 35.5)'/><line x1='5.496' y2='5.496' transform='translate(51.18 40.996)'/></g></svg>
            </button>
        </div>
    </div>
</template>

<script>
import { EventBus } from './../eventBus.js'
import throttle from './../throttle.js'

export default {
    data () {
        return {
            showArrows: false,
            showNextArrow: true,
            showPrevArrow: true,
        }
    },
    methods: {
        resizeBody () {
            this.showArrows = false
            if (!this.$refs.container) return
            if (window.innerWidth > 700) {
                if (this.$refs.container.scrollWidth > window.innerWidth) {
                    document.body.style.height = this.$refs.container.scrollWidth + 'px'
                    window.addEventListener('scroll', this.handleScroll)
                    this.showArrows = true
                }
            } else {
                document.body.style.height = 'auto'
                window.removeEventListener('scroll', this.handleScroll)
            }
        },
        handleScroll () {
            const percentageScrolled = window.scrollY / (document.body.scrollHeight - window.innerHeight)
            this.$refs.container.style.transform = 'translateX(-' + (percentageScrolled * (this.$refs.container.scrollWidth - this.$refs.container.clientWidth)) + 'px)'

            this.showPrevArrow = percentageScrolled > 0.05
            this.showNextArrow = percentageScrolled <= 0.95
        },
        scroll (direction) {
            const movement = this.$refs.container.clientWidth * 0.75 * direction
            window.scrollTo(0, window.scrollY + movement)
        }
    },
    mounted () {
        this.resizeBody()
        this.handleScroll()
        window.addEventListener('resize', this.resizeBody)
        EventBus.$on('workPhoto:resized', throttle(() => {
            this.resizeBody()
        }, 200))
    },
    destroyed () {
        document.body.style.height = 'auto'
        window.removeEventListener('resize', this.resizeBody)
        window.removeEventListener('scroll', this.handleScroll)
    }
}
</script>

<style scoped lang='scss' src='@/scss/horizontal.scss'></style>
