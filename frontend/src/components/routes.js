import About from './pages/About'
import Home from './pages/Home'
import WorkIndex from './pages/Work/WorkIndex'
import Contact from './pages/Contact'

export const routes = [
    { 
        path: '/', 
        component: Home,
    },
    { 
        path: '/about', 
        component: About,
    },
    { 
        path: '/work', 
        component: WorkIndex,
    },
    { 
        path: '/contact', 
        component: Contact,
    }
]
