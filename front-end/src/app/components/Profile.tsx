"use client";

import React, { useState } from "react";
import { useUser } from "@auth0/nextjs-auth0/client";
import { Avatar } from "@nextui-org/react";

export default function Profile() {
  const { user, error, isLoading } = useUser();
  const [isModalOpen, setIsModalOpen] = useState(false);

  const reverseState = () => {
    setIsModalOpen(!isModalOpen);
  };

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>{error.message}</div>;

  return (
    user && (
        <div className="flex ml-auto" onClick={reverseState}>
          <Avatar
            src={user.picture as string}
            className="ml-auto"  
          />
          {isModalOpen && (
            <div className="flex-1">
              <h2 className="text-xl font-semibold">{user.email}</h2>
              <p className="text-gray-600">{user.name}</p>
            </div>
          )}
        </div>
    )
  );
}
