const tl = new TimelineMax();
const tl2 = new TimelineMax();
const tl3 = new TimelineMax();
const tl4 = new TimelineMax();

tl.fromTo("#H_grid1", 1, {opacity: 0}, {opacity: 1, duration: 2}
).fromTo("#H_grid1", 1, {x: "-400"}, {x: '0%', ease: Power2.easeInOut});

tl2.fromTo("#H_grid2", 1, {opacity: 0}, {opacity: 1, duration: 2}
).fromTo("#H_grid2", 1, {x: "400"}, {x: '0%', ease: Power2.easeInOut});


gsap.fromTo("#jc1", .5, {x: "-400"}, {x: '0%', ease: Power2.easeInOut});
gsap.fromTo("#jc2", .5, {x: "400"}, {x: '0%', ease: Power2.easeInOut});

tl3.fromTo(".indv_ref1", 1, {opacity: 0}, {opacity: 1, duration: 2}
).fromTo(".indv_ref1", {x: "-400"}, {rotation: 360, x: 100, duration: 1}
).fromTo(".indv_ref2", 1, {opacity: 0}, {opacity: 1, duration: 2}
).fromTo(".indv_ref2", {x: "400"}, {rotation: 360, x: 100, duration: 1}
).fromTo(".indv_ref3", 1, {opacity: 0}, {opacity: 1, duration: 2}
).fromTo(".indv_ref3", {x: "-400"}, {rotation: 360, x: 100, duration: 1}
).fromTo(".indv_ref1",{scale: 1},{scale: 1.5}).to(".indv_ref1",{scale: 1}
).fromTo(".indv_ref2",{scale: 1},{scale: 1.5}).to(".indv_ref2",{scale: 1}
).fromTo(".indv_ref3",{scale: 1},{scale: 1.5}).to(".indv_ref3",{scale: 1})
;

tl4.fromTo("#skills1",{scale: 1},{scale: 1.5}).to("#skills1",{scale: 1}
).fromTo("#skills2",{scale: 1},{scale: 1.5}).to("#skills2",{scale: 1}
).fromTo("#skills3",{scale: 1},{scale: 1.5}).to("#skills3",{scale: 1})
;


gsap.registerPlugin(ScrollTrigger);
gsap.fromTo(".home_con_title", {opacity: 0}, {opacity: 1, duration: 3, scrollTrigger: ".home_con_title"});
gsap.fromTo("#jc3", {opacity: 0}, {opacity: 1, duration: 3, scrollTrigger: "#jc3"});