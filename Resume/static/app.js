const tl = new TimelineMax();
const tl2 = new TimelineMax();

tl.fromTo("#H_grid1", 1, {opacity: 0}, {opacity: 1, duration: 2}
).fromTo("#H_grid1", 1, {x: "-400"}, {x: '0%', ease: Power2.easeInOut});

tl2.fromTo("#H_grid2", 1, {opacity: 0}, {opacity: 1, duration: 2}
).fromTo("#H_grid2", 1, {x: "400"}, {x: '0%', ease: Power2.easeInOut});

gsap.fromTo(".job_container", {opacity: 0}, {opacity: 1, duration: 2});
gsap.fromTo(".job_container", 1.2, {y: "-400"}, {y: '0%', ease: Power2.easeInOut});

gsap.registerPlugin(ScrollTrigger);
gsap.fromTo(".home_con_title", {opacity: 0}, {opacity: 1, duration: 3, scrollTrigger: ".home_con_title"});