<template>
    <div>
        <slot></slot>
    </div>
</template>

<script>
export default {
    methods: {
        resizeBody () {
            if (window.innerWidth > 700) {
                document.body.style.height = this.$el.scrollWidth + 'px'
                window.addEventListener('scroll', this.handleScroll)
            } else {
                document.body.style.height = 'auto'
                window.removeEventListener('scroll', this.handleScroll)
            }
        },
        handleScroll () {
            const percentageScrolled = window.scrollY / (document.body.scrollHeight - window.innerHeight)
            this.$el.style.transform = 'translateX(-' + (percentageScrolled * (this.$el.scrollWidth - window.innerWidth)) + 'px)'
        }
    },
    mounted () {
        this.resizeBody()
        window.addEventListener('resize', this.resizeBody)
    },
    destroyed () {
        document.body.style.height = 'auto'
        window.removeEventListener('resize', this.resizeBody)
        window.removeEventListener('scroll', this.handleScroll)
    }
}
</script>
