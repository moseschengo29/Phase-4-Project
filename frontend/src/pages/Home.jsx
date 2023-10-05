import AppointmentSection from "../ui/AppointmentSection";
import Banner from "../ui/Banner";
import Gallery from "../ui/Gallery";
import ServicesSection from "../ui/ServicesSection";

function Home() {
  return (
    <>
      <Banner />
      <ServicesSection />
      <Gallery />
      <AppointmentSection />
    </>
  );
}

export default Home;
