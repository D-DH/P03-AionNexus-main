import { redirect } from 'next/navigation'
import Profile from "./components/Profile";
import SearchComponent from "./components/SearchComponent";
import TableComponent from "./components/TableComponent";
import { getSession } from "@auth0/nextjs-auth0";
import NavBar from './components/NavBar';
import { NextUIProvider } from '@nextui-org/react';

export default async function Home() {
  const user = await getSession();
  console.log(user)
  
  if (!user) {
    redirect("/api/auth/login");
  }

  return (
      <main>
        {user && 
          <div>
            <NextUIProvider>
            <NavBar/>
            {/* <SearchComponent></SearchComponent> */}
            <TableComponent></TableComponent>
            </NextUIProvider>
          </div>
        }
      </main>
  );
}
