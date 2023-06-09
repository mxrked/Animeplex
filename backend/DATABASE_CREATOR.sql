USE [Animeplex]
GO
/****** Object:  Table [dbo].[Anime]    Script Date: 5/30/2023 10:03:44 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Anime](
	[Anime_ID] [int] IDENTITY(1,1) NOT NULL,
	[Anime_Name] [nvarchar](max) NULL,
	[Anime_Watched] [bit] NULL,
	[Anime_Favorited] [bit] NULL,
 CONSTRAINT [PK_Anime] PRIMARY KEY CLUSTERED 
(
	[Anime_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Users]    Script Date: 5/30/2023 10:03:44 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Users](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[User_Email] [nvarchar](max) NULL,
	[User_Password] [nvarchar](max) NULL,
	[User_Watched_Array] [nvarchar](max) NULL,
	[User_Favorites_Array] [nvarchar](max) NULL,
 CONSTRAINT [PK_Users] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
